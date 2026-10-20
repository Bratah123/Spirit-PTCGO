"""STUB: effect not implemented — do not guess mechanics.
Altaria-EX (XY10 #123): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive


async def _cavalry_lance(ctx):
    """Printed damage; during your opponent's next turn this Pokémon has no Weakness."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, no_weakness_passive())


card = PokemonCardDef(
    guid="0f1ec2c7-b413-55c5-998e-1fc3b76cf7fe",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AltariaEX.Name",
    display_name="Altaria-EX",
    searchable_by=["Altaria-EX", "Basic", "EX", "AltariaEX"],
    subtypes=["Basic", "EX"],
    collector_number=123,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=334,
    abilities=[
        Attack(
            title="Powerful Gain",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 60 more damage and heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shining Wind",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            # STUB: attack effect not implemented
            effect=_cavalry_lance,
        ),
    ],
)