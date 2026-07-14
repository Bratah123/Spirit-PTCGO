from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches, remove_self_from_play


async def fan_tornado(ctx):
    """50. You may have your opponent switch their Active with 1 of their Benched Pokemon."""
    await ctx.deal_damage()
    if not ctx.opponent_bench():
        return
    if await ctx.ask_yes_no(
            "Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="e1e3b13c-790e-500a-b26e-e72d8bd3af1a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Fan Tornado",
            game_text="You may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=fan_tornado,
        ),
        Attack(
            title="Tearing Gust",
            game_text="Put this Pokémon and all attached cards in the Lost Zone.",
            cost={PokemonTypes.GRASS: 1},
            damage=210,
            effect=remove_self_from_play("lost_zone"),
        ),
    ],
)
