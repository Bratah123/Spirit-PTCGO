"""Author and validate the bot decks for the queue AI.

Usage:
    python spirit/tools/build_bot_decks.py                # validate DECKS below + print a BOT_DECK_LISTS block
    python spirit/tools/build_bot_decks.py --check        # validate the lists committed in bot_decks.py
    python spirit/tools/build_bot_decks.py --from-folder  # turn spirit/tools/DECKS/*.txt into a pool
    python spirit/tools/build_bot_decks.py --from-folder --emit
        # ... and write spirit/game/content/bot_decks_scraped.py (the bot's
        #     scraped pool, merged into BOT_DECK_LISTS at import time)

Both modes enforce the same rules the client does: exactly 60 cards, at least
one Basic Pokemon, the four-copy limit (basic energy exempt). Energy coverage
is reported too -- the deck must pay for at least one Pokemon's attack (hard
error), while big attackers the list never attacks with are only warnings.

Workflow for a new hand-made deck:
  1. add a name-token list to DECKS below, e.g. (4, "CharizardV"),
  2. run this script with no args and read the [OK]/[BAD] report,
  3. paste the emitted block into HAND_CURATED in spirit/game/content/bot_decks.py,
  4. run `--check` and restart the server.

Workflow for a deck scraped into spirit/tools/DECKS/*.txt: run
`--from-folder --emit`, then `--check`, then restart the server.
"""
import json
import logging
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
TOOLS_DIR = ROOT / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

logging.disable(logging.INFO)

import convert_deck  # noqa: E402  (repo tools/, owns the deck list formats)
from spirit.game.scripts.cards import loader  # noqa: E402
from spirit.game.attributes import AttrID, PokemonTypes  # noqa: E402
from spirit.game.content.definitions import ability_id_for, ABILITIES_BY_ID  # noqa: E402
from spirit.game.content.starter import SET_CODE_MAP  # noqa: E402

cards = loader.load_all()
DECKS_DIR = ROOT / "spirit" / "tools" / "DECKS"
SCRAPED_MODULE = ROOT / "spirit" / "game" / "content" / "bot_decks_scraped.py"

STANDARD_SETS = ["SWSH12", "SWSH11", "SWSH10", "SWSH9", "SWSH8", "SWSH7", "SWSH6",
                 "SWSH5", "SWSH4", "SWSH3", "SWSH35", "SWSH2", "SWSH45", "SWSH1",
                 "CEL25", "PGO", "CZ", "Free_Energy"]
SET_RANK = {s: i for i, s in enumerate(STANDARD_SETS)}
LIVE_CODE = {"SWSH1": "SSH", "SWSH2": "RCL", "SWSH3": "DAA", "SWSH35": "CPA",
             "SWSH4": "VIV", "SWSH45": "SHF", "SWSH5": "BST", "SWSH6": "CRE",
             "SWSH7": "EVS", "SWSH8": "FST", "SWSH9": "BRS", "SWSH10": "ASR",
             "SWSH11": "LOR", "SWSH12": "SIT", "CEL25": "CEL", "PGO": "PGO",
             "CZ": "CRZ", "Free_Energy": "Free_Energy"}

# Cards whose plain id is the display name (energies) resolve exactly; the rest
# are matched on the archetype token inside com.direwolfdigital...archetypes.X.Name
ENERGY_NAMES = {
    "FireEnergy": "Fire Energy", "WaterEnergy": "Water Energy",
    "LightningEnergy": "Lightning Energy", "PsychicEnergy": "Psychic Energy",
    "DarknessEnergy": "Darkness Energy", "FightingEnergy": "Fighting Energy",
    "GrassEnergy": "Grass Energy", "MetalEnergy": "Metal Energy",
    "FairyEnergy": "Fairy Energy", "DoubleTurboEnergy": "Double Turbo Energy",
    "PowerfulColorlessEnergy": "Powerful Colorless Energy",
    "RapidStrikeEnergy": "Rapid Strike Energy", "SingleStrikeEnergy": "Single Strike Energy",
    "AuroraEnergy": "Aurora Energy", "CaptureEnergy": "Capture Energy",
    "SpeedLightningEnergy": "Speed Lightning Energy", "TwinEnergy": "Twin Energy",
    "HeatFireEnergy": "Heat Fire Energy", "HorrorPsychicEnergy": "Horror Psychic Energy",
    "VGuardEnergy": "V Guard Energy", "RegenerativeEnergy": "Regenerative Energy",
    "GiftEnergy": "Gift Energy", "TreasureEnergy": "Treasure Energy",
}


def display(c):
    d = c.display_name
    if isinstance(d, str) and d:
        return d
    raw = str(c.get_attribute_value(AttrID.NAME))
    if raw.startswith('{"id": "'):
        return raw.split('"')[3]
    return raw


def norm(s):
    return s.lower().replace(" ", "").replace("'", "").replace("-", "")


def is_basic_energy(card):
    if str(card.get_attribute_value(AttrID.CARD_TYPE)) != "3":
        return False
    return not bool(card.get_attribute_value(AttrID.IS_SPECIAL_ENERGY))


def energy_types(card):
    """Set of PokemonTypes this energy can provide (across its option groups)."""
    type_by_value = {int(t.value): t.name for t in PokemonTypes}
    types = set()
    info = card.get_attribute_value(AttrID.ENERGY_INFO)
    options = None
    if isinstance(info, str) and info.strip().startswith("{"):
        try:
            options = json.loads(info).get("options", [])
        except ValueError:
            options = None
    elif isinstance(info, (list, tuple)):
        options = info
    if options:
        for group in options:
            if not group:
                continue
            for v in group:
                if isinstance(v, (int, float)):
                    types.add(type_by_value.get(int(v), str(v)))
                else:
                    types.add(str(getattr(v, "name", v)))
    if not types and is_basic_energy(card):
        n = norm(display(card)).replace("energy", "").strip("_")
        if n:
            types.add(n.upper())
    return types


def candidates(token):
    if token.startswith("Basic"):
        token = token[5:]
    if token in ENERGY_NAMES:
        want = norm(ENERGY_NAMES[token])
        return [c for c in cards if norm(display(c)) == want]
    t = norm(token)
    exact = [c for c in cards if norm(display(c)) == t]
    if exact:
        # Exact name wins: substring hits on the archetype id otherwise pick
        # neighbours ('Switch' -> Energy Switch, 'Marnie' -> Marnie's Pride).
        return exact
    out = []
    for c in cards:
        raw = str(c.get_attribute_value(AttrID.NAME)).lower()
        if "archetypes" in raw and t in raw.replace(" ", "").replace("'", ""):
            out.append(c)
    return out


def pick(token, set_hint=None):
    cands = [c for c in candidates(token) if c.key in SET_RANK]
    if not cands:
        return None, candidates(token)
    if set_hint:
        hinted = [c for c in cands if c.key == set_hint]
        if hinted:
            cands = hinted
    cands.sort(key=lambda c: (SET_RANK[c.key],
                              int(c.get_attribute_value(AttrID.COLLECTOR_NUMBER) or 0)))
    return cands[0], cands


def attacks_of(card):
    res = []
    for slot in range(6):
        a = ABILITIES_BY_ID.get(ability_id_for(card.guid, slot))
        if a is None:
            continue
        res.append((getattr(a, "title", ""), getattr(a, "cost", None),
                    getattr(a, "damage", None), type(a).__name__))
    return res


DECKS = {
    "Charizard VSTAR": [
        (4, "CharizardV"), (3, "CharizardVSTAR"), (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (4, "Marnie"), (3, "Raihan"), (2, "BosssOrders"),
        (1, "Serena"), (4, "QuickBall"), (3, "UltraBall"), (2, "LevelBall"),
        (3, "ChoiceBelt"), (3, "EscapeRope"), (3, "Switch"), (3, "EnergyRetrieval"),
        (1, "PalPad"), (1, "BigCharm"), (1, "LostVacuum"), (1, "ForestSealStone"),
        (10, "FireEnergy"), (2, "HeatFireEnergy"),
    ],
    "Arceus Duraludon": [
        (4, "ArceusV"), (3, "ArceusVSTAR"), (3, "DuraludonV"), (2, "DuraludonVMAX"),
        (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (2, "Serena"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (4, "EvolutionIncense"), (2, "RareCandy"),
        (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"), (1, "AirBalloon"),
        (2, "EnergyRetrieval"), (1, "PalPad"), (1, "PathToThePeak"),
        (6, "MetalEnergy"), (2, "FightingEnergy"), (4, "DoubleTurboEnergy"),
        (3, "PowerfulColorlessEnergy"),
    ],
    "Rapid Strike Urshifu": [
        (4, "RapidStrikeUrshifuV"), (3, "RapidStrikeUrshifuVMAX"), (2, "Octillery"),
        (3, "Sobble"), (2, "Drizzile"), (1, "Inteleon"), (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (1, "KorrinasFocus"), (2, "BosssOrders"),
        (3, "QuickBall"), (3, "UltraBall"), (2, "LevelBall"), (2, "EvolutionIncense"),
        (1, "RareCandy"), (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"),
        (1, "TowerofWaters"), (1, "PalPad"),
        (6, "FightingEnergy"), (4, "BasicWaterEnergy"), (4, "RapidStrikeEnergy"),
    ],
    "Single Strike Urshifu": [
        (4, "SingleStrikeUrshifuV"), (3, "SingleStrikeUrshifuVMAX"), (4, "Houndour"),
        (3, "Houndoom"), (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (2, "KorrinasFocus"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (3, "LevelBall"), (2, "EvolutionIncense"),
        (2, "RareCandy"), (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"),
        (1, "TowerofDarkness"), (1, "PalPad"), (1, "BigCharm"),
        (8, "FightingEnergy"), (3, "BasicDarknessEnergy"), (4, "SingleStrikeEnergy"),
    ],
    "Ice Rider Calyrex": [
        (4, "IceRiderCalyrexV"), (3, "IceRiderCalyrexVMAX"), (4, "Glastrier"),
        (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (4, "Irida"), (1, "Klara"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (3, "LevelBall"), (2, "EvolutionIncense"),
        (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"), (2, "EnergyRetrieval"),
        (1, "PalPad"), (1, "PathToThePeak"), (1, "FogCrystal"),
        (12, "BasicWaterEnergy"), (3, "DoubleTurboEnergy"),
    ],
    "Shadow Rider Calyrex": [
        (4, "ShadowRiderCalyrexV"), (3, "ShadowRiderCalyrexVMAX"), (4, "Spectrier"),
        (1, "LumineonV"), (1, "Manaphy"), (1, "Cramorant"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (3, "Adaman"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (3, "LevelBall"), (3, "FogCrystal"),
        (2, "EvolutionIncense"), (2, "EscapeRope"), (2, "Switch"), (1, "AirBalloon"),
        (2, "EnergyRetrieval"), (1, "PalPad"), (1, "PathToThePeak"),
        (12, "BasicPsychicEnergy"), (3, "DoubleTurboEnergy"),
    ],
    "Eternatus VMAX": [
        (4, "EternatusV"), (3, "EternatusVMAX"), (3, "CrobatV"), (3, "Zubat"),
        (2, "Golbat"), (2, "Eiscue"), (1, "LumineonV"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (3, "Judge"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (2, "LevelBall"), (2, "EvolutionIncense"),
        (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"), (1, "AirBalloon"),
        (2, "EnergyRetrieval"), (1, "PalPad"), (1, "BigCharm"),
        (14, "BasicDarknessEnergy"), (3, "CaptureEnergy"),
    ],
    "Rayquaza VMAX": [
        (4, "RayquazaV"), (3, "RayquazaVMAX"), (2, "Joltik"), (2, "Flaaffy"),
        (3, "Electrike"), (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (1, "ZinniasResolve"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (2, "LevelBall"), (1, "EvolutionIncense"),
        (1, "RareCandy"), (1, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"),
        (1, "TrainingCourt"), (1, "PalPad"),
        (8, "BasicLightningEnergy"), (5, "BasicFireEnergy"), (3, "AuroraEnergy"),
    ],
    "Origin Palkia VSTAR": [
        (4, "OriginFormePalkiaV"), (3, "OriginFormePalkiaVSTAR"), (3, "RadiantGreninja"),
        (4, "Comfey"), (2, "Cramorant"), (2, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (3, "Irida"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (3, "LevelBall"), (2, "FogCrystal"),
        (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"), (2, "EnergyRetrieval"),
        (1, "PalPad"), (1, "PathToThePeak"), (1, "TrainingCourt"),
        (12, "BasicWaterEnergy"), (4, "DoubleTurboEnergy"),
    ],
    "Flying Pikachu VMAX": [
        (4, "FlyingPikachuV"), (3, "FlyingPikachuVMAX"), (3, "Pikachu"),
        (2, "Raichu"), (1, "BoltundV"), (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (2, "Judge"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (2, "LevelBall"), (1, "EvolutionIncense"),
        (1, "RareCandy"), (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"),
        (1, "TowerofWaters"), (1, "PalPad"),
        (9, "BasicLightningEnergy"), (4, "SpeedLightningEnergy"), (3, "CaptureEnergy"),
    ],
    "Giratina VSTAR": [
        (4, "GiratinaV"), (3, "GiratinaVSTAR"), (4, "Comfey"), (1, "Cramorant"),
        (1, "Sableye"), (1, "LumineonV"), (1, "Manaphy"),
        (4, "ColresssExperiment"), (3, "ProfessorsResearch"), (2, "Klara"), (2, "BosssOrders"),
        (4, "QuickBall"), (2, "UltraBall"), (2, "LevelBall"), (4, "MirageGate"),
        (1, "BattleVIPPass"), (2, "EscapeRope"), (2, "Switch"), (1, "LostVacuum"),
        (1, "PalPad"),
        (6, "BasicGrassEnergy"), (6, "BasicPsychicEnergy"), (4, "DoubleTurboEnergy"),
    ],
    "Gengar VMAX": [
        (4, "GengarV"), (3, "GengarVMAX"), (4, "Gastly"), (3, "Haunter"),
        (2, "CrobatV"), (1, "LumineonV"), (1, "Manaphy"),
        (4, "ProfessorsResearch"), (3, "Marnie"), (3, "Judge"), (2, "BosssOrders"),
        (4, "QuickBall"), (3, "UltraBall"), (3, "LevelBall"), (2, "EvolutionIncense"),
        (2, "RareCandy"), (2, "ChoiceBelt"), (2, "EscapeRope"), (2, "Switch"),
        (1, "TowerofDarkness"), (1, "PalPad"), (1, "BigCharm"),
        (12, "BasicDarknessEnergy"), (3, "HorrorPsychicEnergy"),
    ],
}


def balance(entries):
    """Pad/trim the biggest basic-energy stack so the deck lands on exactly 60."""
    resolved = [(e, pick(e[1])[0]) for e in entries]
    total = sum(e[0] for e, _ in resolved)
    delta = 60 - total
    if delta == 0:
        return list(entries), None
    idx = None
    for i, (e, card) in enumerate(resolved):
        if card is not None and is_basic_energy(card):
            if idx is None or e[0] > resolved[idx][0][0]:
                idx = i
    if idx is None:
        return None, f"delta {delta:+d} but no basic energy to absorb it"
    count, token = entries[idx]
    new_count = count + delta
    if not 1 <= new_count <= 14:
        return None, f"delta {delta:+d} pushes {token} to {new_count}"
    out = list(entries)
    out[idx] = (new_count, token)
    return out, None


def _attacks_payable(card, provided):
    """(has_attack, any_attack_payable) for one Pokemon card."""
    has_attack = False
    for title, cost, _dmg, kind in attacks_of(card):
        if kind != "Attack" or not cost:
            continue
        has_attack = True
        gaps = 0
        for ptype, n in cost.items():
            tname = str(getattr(ptype, "name", ptype)).upper()
            if tname == "COLORLESS":
                continue
            if provided[tname] < n:
                gaps += 1
        if not gaps:
            return True, True
    return has_attack, False


def coverage(pokes, provided):
    """Energy gap report: errors only when nothing can attack.

    A deck must pay for at least one Pokemon's attack (otherwise the bot can
    never act).  Support lines (Inteleon, engine Zacian V, ...) that cannot
    pay are reported as warnings instead, since lists never attack with them.
    """
    gaps = []
    attackers = 0
    for label, card in pokes:
        has_attack, payable = _attacks_payable(card, provided)
        if not has_attack:
            continue
        if payable:
            attackers += 1
            continue
        hp = card.hp or 0
        main = hp >= 200 or getattr(card, "stage", None) == 2
        for title, cost, _dmg, kind in attacks_of(card):
            if kind != "Attack" or not cost:
                continue
            need = {}
            for ptype, n in cost.items():
                tname = str(getattr(ptype, "name", ptype)).upper()
                if tname != "COLORLESS":
                    need[tname] = n
            missing = [f"{n} {t}" for t, n in need.items() if provided[t] < n]
            if missing:
                gaps.append((0 if main else 1, hp,
                             f"can't pay: {label} '{title}' needs {'+'.join(missing)}"
                             f" (deck has {'/'.join(str(provided[t]) for t in need)})"))
                break
    issues, warns = [], []
    if pokes and attackers == 0:
        issues.append("no Pokemon in the deck can pay for any attack")
    for _is_main, _hp, msg in sorted(gaps, key=lambda g: (g[0], -g[1])):
        warns.append(msg)
    return issues, warns


def build(name, entries):
    issues = []
    refs = []
    total = 0
    basics = 0
    resolved_cards = []
    entries, bal_err = balance(entries)
    if bal_err:
        issues.append(f"balance: {bal_err}")
        entries = [e for e in DECKS[name]]
    for count, token in entries:
        card, _ = pick(token)
        if card is None:
            issues.append(f"missing: {token}")
            continue
        num = int(card.get_attribute_value(AttrID.COLLECTOR_NUMBER))
        refs.append((count, LIVE_CODE[card.key], num))
        resolved_cards.append((count, token, card))
        total += count
        ctype = str(card.get_attribute_value(AttrID.CARD_TYPE))
        if ctype == "0" and getattr(card, "stage", None) == 0:
            basics += count
        if ctype != "0" and not is_basic_energy(card) and count > 4:
            issues.append(f"over 4x: {token} x{count}")
    if total != 60:
        issues.append(f"total={total} (need 60, delta {60 - total:+d})")
    if basics < 1:
        issues.append("no basic Pokemon")
    return refs, issues, resolved_cards, total, basics


def report(name, issues, warns, total, basics, npoke, energy):
    status = "OK " if not issues else "BAD"
    print(f"[{status}] {name}: total={total} basics={basics} pokes={npoke}")
    for i in issues:
        print(f"        ! {i}")
    for w in warns:
        print(f"        - {w}")
    print(f"        energy: {dict(energy)}")
    return status == "OK "


def card_lookup():
    """(local set, collector number) -> card, plus display name -> [cards]."""
    by_ref = {}
    by_name = {}
    for card in cards:
        num = card.get_attribute_value(AttrID.COLLECTOR_NUMBER)
        if num is not None:
            try:
                by_ref[(card.key.upper(), int(num))] = card
            except (TypeError, ValueError):
                pass
        by_name.setdefault(norm(display(card)), []).append(card)
    return by_ref, by_name


def _card_by_name(cands):
    return min(cands, key=lambda c: (SET_RANK.get(c.key, 99),
                                     int(c.get_attribute_value(AttrID.COLLECTOR_NUMBER) or 0)))


def refs_from_file(path: Path, by_ref, by_name):
    """(refs, problems) for one saved .txt deck; refs are (count, live set, number)."""
    refs, problems = [], []
    text = path.read_text(encoding="utf-8-sig")
    for _section, count, cname, set_code, number in convert_deck.parse_card_lines(text):
        card = None
        if set_code and number and number.isdigit():
            local = SET_CODE_MAP.get(set_code.upper(), set_code.upper())
            card = by_ref.get((local.upper(), int(number)))
        if card is not None:
            refs.append((count, LIVE_CODE.get(card.key, card.key),
                         int(card.get_attribute_value(AttrID.COLLECTOR_NUMBER))))
            continue
        # no set on the line (basic energies), or a reference this catalog
        # doesn't know: fall back to the printed name
        cands = by_name.get(norm(cname))
        if not cands:
            problems.append(f"missing: {cname}"
                            + (f" ({set_code} {number})" if set_code else ""))
            continue
        card = _card_by_name(cands)
        num = card.get_attribute_value(AttrID.COLLECTOR_NUMBER)
        try:
            num = int(num)
        except (TypeError, ValueError):
            problems.append(f"missing: {cname}")
            continue
        refs.append((count, LIVE_CODE.get(card.key, card.key), num))
    return refs, problems


def validate_refs(name, refs, by_ref):
    """Same rules as build(): counts, basics, four-copy, energy coverage."""
    issues = []
    resolved = []
    total = 0
    basics = 0
    for count, live, number in refs:
        local = SET_CODE_MAP.get(live, live)
        card = by_ref.get((local.upper(), int(number)))
        if card is None:
            issues.append(f"missing: {live} {number}")
            continue
        label = display(card)
        resolved.append((count, label, card))
        total += count
        ctype = str(card.get_attribute_value(AttrID.CARD_TYPE))
        if ctype == "0" and getattr(card, "stage", None) == 0:
            basics += count
        if ctype != "0" and not is_basic_energy(card) and count > 4:
            issues.append(f"over 4x: {label} x{count}")
    if total != 60:
        issues.append(f"total={total} (need 60, delta {60 - total:+d})")
    if basics < 1:
        issues.append("no basic Pokemon")

    energy = Counter()
    provided = Counter()
    pokes = []
    for count, label, card in resolved:
        ctype = str(card.get_attribute_value(AttrID.CARD_TYPE))
        if ctype == "3":
            energy[label] += count
            for t in energy_types(card):
                provided[t.upper()] += count
        elif ctype == "0":
            pokes.append((label, card))
    issues += coverage(pokes, provided)[0]
    warns = coverage(pokes, provided)[1]
    npoke = sum(c for c, _l, x in resolved
                if str(x.get_attribute_value(AttrID.CARD_TYPE)) == "0")
    return issues, warns, total, basics, npoke, energy, resolved


def from_folder(emit=False):
    """Validate spirit/tools/DECKS/*.txt and (with --emit) regenerate the pool."""
    if not DECKS_DIR.is_dir():
        print(f"no deck folder: {DECKS_DIR}")
        return 1
    by_ref, by_name = card_lookup()
    good = {}
    all_ok = True
    paths = sorted(DECKS_DIR.glob("*.txt"))
    print(f"{len(paths)} deck file(s) in {DECKS_DIR}\n")
    for path in paths:
        name = path.stem
        refs, problems = refs_from_file(path, by_ref, by_name)
        issues, warns, total, basics, npoke, energy, resolved = validate_refs(
            name, refs, by_ref)
        issues = problems + issues
        all_ok &= report(name, issues, warns, total, basics, npoke, energy)
        if not issues:
            good[name] = (refs, resolved)

    print(f"\n{len(good)} usable / {len(paths)} total")
    if not emit:
        return 0 if all_ok else 1
    if not all_ok:
        print("not emitting: fix or move the failing decks first")
        return 1
    emit_scraped(good, by_ref)
    return 0


def emit_scraped(good, by_ref):
    """Write spirit/game/content/bot_decks_scraped.py from validated decks."""
    lines = [
        '"""Scraped bot decks -- generated file, do not edit by hand.',
        '',
        'Regenerate with:',
        '    python spirit/tools/build_bot_decks.py --from-folder --emit',
        'Sources: spirit/tools/DECKS/*.txt (Limitless top lists, converted for',
        'this client by tools/convert_deck.py and checked against the catalog).',
        '"""',
        '',
        "SCRAPED_DECK_LISTS = {",
    ]
    for name in sorted(good):
        refs, resolved = good[name]
        lines.append(f"    {name!r}: [")
        for (count, live, number), (_c, label, _card) in zip(refs, resolved):
            lines.append(f"        ({count}, {live!r}, {number}),   # {label}")
        lines.append("    ],")
        lines.append("")
    lines.append("}")
    SCRAPED_MODULE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nwrote {len(good)} decks -> {SCRAPED_MODULE}")


def author():
    all_ok = True
    for name, entries in DECKS.items():
        refs, issues, resolved, total, basics = build(name, entries)
        energy = Counter()
        provided = Counter()
        pokes = []
        for count, token, card in resolved:
            ctype = str(card.get_attribute_value(AttrID.CARD_TYPE))
            if ctype == "3":
                energy[token] += count
                for t in energy_types(card):
                    provided[t.upper()] += count
            elif ctype == "0":
                pokes.append((token, card))
        issues += coverage(pokes, provided)[0]
        warns = coverage(pokes, provided)[1]
        npoke = sum(c for c, t, x in resolved
                    if str(x.get_attribute_value(AttrID.CARD_TYPE)) == "0")
        all_ok &= report(name, issues, warns, total, basics, npoke, energy)

    if not all_ok:
        return 1
    print("\nALL DECKS VALID\n")
    print("BOT_DECK_LISTS = {")
    for name, entries in DECKS.items():
        refs, _, resolved, _, _ = build(name, entries)
        print(f"    {name!r}: [")
        for (count, code, num), (_, _, card) in zip(refs, resolved):
            print(f"        ({count}, {code!r}, {num}),   # {display(card)}")
        print("    ],")
        print()
    print("}")
    return 0


def check_committed():
    """Validate the lists that actually ship in spirit/game/content/bot_decks.py."""
    from spirit.game.content.bot_decks import BOT_DECK_LISTS
    from spirit.game.content.starter import build_deck_data

    all_ok = True
    for name, decklist in BOT_DECK_LISTS.items():
        issues = []
        warns = []
        deck = build_deck_data(name, decklist)
        pile = deck.get("piles", {}).get("deck") or []
        if len(pile) != 60:
            issues.append(f"total={len(pile)} (need 60, delta {60 - len(pile):+d})")
        counts = Counter()
        energy = Counter()
        provided = Counter()
        pokes = []
        basics = 0
        npoke = 0
        for guid in pile:
            card = loader.cards_by_guid.get(guid.lower())
            if card is None:
                issues.append(f"unknown guid {guid}")
                continue
            counts[card.guid] += 1
            ctype = str(card.get_attribute_value(AttrID.CARD_TYPE))
            if ctype == "0":
                npoke += 1
                if getattr(card, "stage", None) == 0:
                    basics += 1
            elif ctype == "3":
                energy[display(card)] += 1
                for t in energy_types(card):
                    provided[t.upper()] += 1
        for card_guid, n in counts.items():
            card = loader.cards_by_guid.get(card_guid.lower())
            if card is None:
                continue
            if str(card.get_attribute_value(AttrID.CARD_TYPE)) != "0" \
                    and not is_basic_energy(card) and n > 4:
                issues.append(f"over 4x: {display(card)} x{n}")
        seen = set()
        for guid in pile:
            card = loader.cards_by_guid.get(guid.lower())
            if card is None or card.guid in seen:
                continue
            seen.add(card.guid)
            if str(card.get_attribute_value(AttrID.CARD_TYPE)) == "0":
                pokes.append((display(card), card))
        if basics < 1:
            issues.append("no basic Pokemon")
        issues += coverage(pokes, provided)[0]
        warns = coverage(pokes, provided)[1]
        all_ok &= report(name, issues, warns, len(pile), basics, npoke, energy)
    print("\nALL COMMITTED DECKS VALID" if all_ok else "\nCOMMITTED DECKS HAVE ISSUES")
    return 0 if all_ok else 1


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check_committed())
    if "--from-folder" in sys.argv:
        sys.exit(from_folder("--emit" in sys.argv))
    sys.exit(author())
