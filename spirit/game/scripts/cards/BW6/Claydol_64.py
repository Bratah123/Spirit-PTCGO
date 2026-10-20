from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.attacks_common import flip_bonus


async def gyro_ball(ctx):
    """Switch self, then opponent switches."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        await ctx.switch_active(ctx.player_id, target or bench[0])
        await ctx.flush_choreography()
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="b92b8eb2-f27b-5ca6-8d61-0e786ceeaa46",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. Then, your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=gyro_ball,
        ),
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_bonus(30),
        ),
    ],
)