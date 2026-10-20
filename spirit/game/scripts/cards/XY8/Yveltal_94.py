"""STUB: effect not implemented — do not guess mechanics.
Yveltal (XY8 #94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.session.passives import carrier_pokemon
from spirit.game.attributes import AttrID
from spirit.game.content.definitions import def_for


class _FrightNight(Passive):
    """As long as this Pokemon is your Active Pokemon, each Pokemon Tool card in play has no effect."""
    def suppresses_tool(self, tool, carrier):
        me = carrier_pokemon(carrier)
        parent = getattr(me, "parent", None)
        return parent is not None and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def _pitch_black_spear(ctx):
    """60; 60 to 1 of your opponent's Benched Pokemon-EX."""
    await ctx.deal_damage()
    pool = [p for p in ctx.opponent_bench() if _is_ex(p)]
    if pool:
        target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Benched Pokémon-EX")
        if target is not None:
            await ctx.deal_damage(60, target=target)


card = PokemonCardDef(
    guid="018b03d0-c370-552f-982c-53eaf2e987b4",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Ability(
            title="Fright Night",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, each Pok\u00e9mon Tool card in play has no effect.",
            # STUB: ability effect not implemented
            passive=_FrightNight(),
        ),
        Attack(
            title="Pitch-Black Spear",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=_pitch_black_spear,
        ),
    ],
)