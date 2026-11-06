from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def future_sight(ctx):
    """Look at the top 5 cards of your deck and put them back in any order."""
    await ctx.reorder_deck_top(5)


card = PokemonCardDef(
    guid="2430e7dc-c043-5c2e-817c-b71ee2a23c0f",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    display_name="Gothita",
    searchable_by=["Gothita", "Basic", "Gothita"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=574,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 5 cards of your deck and put them back on top of your deck in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=future_sight,
        ),
    ],
)