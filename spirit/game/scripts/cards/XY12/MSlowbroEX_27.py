from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import apply_own_next_turn_boost


async def _loll_roll_spin(ctx):
    """100; this Pokemon is now Confused; during your next turn Loll Roll Spin does 100 more."""
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)
    await apply_own_next_turn_boost(ctx, 100, "Loll Roll Spin")


card = PokemonCardDef(
    guid="8d4c9998-4172-5df3-9675-9b2301efd224",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSlowbroEX.Name",
    display_name="M Slowbro-EX",
    searchable_by=["M Slowbro-EX", "MEGA", "EX", "MSlowbroEX"],
    subtypes=["MEGA", "EX"],
    collector_number=27,
    set_code="XY12",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SlowbroEX.Name",
    family_id=80,
    abilities=[
        Attack(
            title="Loll Roll Spin",
            game_text="This Pok\u00e9mon is now Confused. During your next turn, this Pok\u00e9mon's Loll Roll Spin attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            damage_operator="+",
            effect=_loll_roll_spin,
        ),
    ],
)