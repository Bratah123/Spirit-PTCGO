from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def all_the_presents(ctx):
    """Flip until tails; for each heads you may search your deck for a card."""
    heads = await ctx.flip_until_tails("All the Presents")
    if heads <= 0:
        return
    picks = await ctx.search_deck(
        None, count=heads, minimum=0,
        prompt="Choose cards to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="fed0f65d-a804-5bd2-aaa7-ad767c82c65a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Attack(
            title="All the Presents",
            game_text="Flip a coin until you get tails. For each heads, you may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=all_the_presents,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)