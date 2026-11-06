from spirit.game.data_utils import PokemonCardDef, Attack, Ability, ABILITIES_BY_ID
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon, effective_attack_cost
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.models.board import PlayArea, PokemonEntity
from spirit.game.session.legal_actions import attack_cost_satisfied


def _opposing_active(target):
    """The opponent's Active Pokemon, found by walking the entity tree (the
    effect-shield and type hooks get no board)."""
    root = target
    while root.parent is not None:
        root = root.parent
    stack = [root]
    while stack:
        node = stack.pop()
        if isinstance(node, PlayArea) and node.get_attribute(AttrID.NAME) == "activePokemonArea" \
                and node.owning_player_id not in (None, target.owning_player_id):
            return next((c for c in node.children if isinstance(c, PokemonEntity)), None)
        stack.extend(node.children)
    return None


class _ColorChangePassive(Passive):
    """While this Pokemon is your Active, it is the same type as your
    opponent's Active Pokemon (its printed types)."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier) or not is_in_active_spot(pokemon):
            return types
        other = _opposing_active(pokemon)
        printed = list(other.get_attribute(AttrID.POKEMON_TYPES) or []) if other is not None else []
        return printed or types


def _payable_attacks(ctx, defender):
    me = ctx.attacker
    energies = ctx.attached_energies(me)
    out = []
    for entry in defender.get_attribute(AttrID.PIE_ABILITIES) or []:
        if not (isinstance(entry, dict) and entry.get("abilityType") == "Attack"):
            continue
        attack = ABILITIES_BY_ID.get(entry.get("abilityID"))
        if attack is None:
            continue
        cost = effective_attack_cost(ctx.board, me, entry.get("cost") or {})
        if attack_cost_satisfied(cost, energies, ctx.board):
            out.append((defender, attack))
    return out


async def _imittack(ctx):
    """Choose 1 of the Defending Pokemon's attacks. If this Pokemon has the
    Energy to use it, use it as this attack."""
    defender = ctx.defender
    if defender is None:
        return
    candidates = _payable_attacks(ctx, defender)
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is not None:
        await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="525953ca-598a-5dfb-abee-966acf3dd4ea",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Kecleon"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Color Change",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, this Pok\u00e9mon is the same type as the your opponent's Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_ColorChangePassive(),
        ),
        Attack(
            title="Imittack",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. If this Pok\u00e9mon has the necessary Energy to use that attack, use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_imittack,
        ),
    ],
)