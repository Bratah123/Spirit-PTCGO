from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def gyro_ball(ctx):
    """Switch self with a Benched Pokemon; if you do, the opponent switches too."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    await ctx.switch_active(ctx.player_id, target or bench[0])
    await ctx.flush_choreography()
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="37bcbf58-8ef1-5834-b648-728a1c85a641",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=130,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Smack",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
        Attack(
            title="Gyro Ball",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, your opponent switches their Active Pokémon with 1 of their Benched Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=gyro_ball,
        ),
    ],
)
