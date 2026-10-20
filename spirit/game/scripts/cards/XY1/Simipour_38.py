from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def garbage_collection(ctx):
    """Put a card from your discard pile on top of your deck."""
    pile = list(ctx.discard_pile())
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, prompt="Choose a card to put on top of your deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = PokemonCardDef(
    guid="d6395e33-bed5-53ab-baf7-a2c1b89e6a4e",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name",
    display_name="Simipour",
    searchable_by=["Simipour", "Stage 1", "Simipour"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    family_id=515,
    abilities=[
        Attack(
            title="Recycle",
            game_text="Put a card from your discard pile on top of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=garbage_collection,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)