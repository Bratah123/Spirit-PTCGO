from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def teatime(ctx):
    """Each player draws 2 cards."""
    await ctx.draw_cards(2)
    await ctx.draw_cards(2, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="83a0d518-80bc-543a-9287-0a6d4b0759e5",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    display_name="Sinistea",
    searchable_by=["Sinistea", "Basic", "Sinistea"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=854,
    abilities=[
        Attack(
            title="Teatime",
            game_text="Each player draws 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=teatime,
        ),
    ],
)