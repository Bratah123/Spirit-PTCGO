from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play


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
    guid="765536ab-044a-5409-8f5f-6e560fba7841",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=489,
    abilities=[
        Attack(
            title="Pull Out",
            game_text="Put a card from your discard pile on top of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=garbage_collection,
        ),
        Attack(
            title="Aqua Boomerang",
            game_text="Return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=remove_self_from_play("hand"),
        ),
    ],
)