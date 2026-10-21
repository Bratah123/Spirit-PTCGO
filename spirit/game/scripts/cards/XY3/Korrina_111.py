from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes, TrainerType
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.trainers import deck_nonempty


def _is_fighting_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.FIGHTING.value in (
        card.get_attribute(AttrID.POKEMON_TYPES) or [])


def _is_item(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.ITEM.value, TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def korrina(ctx):
    """Search your deck for a Fighting Pokemon and an Item card, reveal them,
    and put them into your hand. Shuffle."""
    groups = await ctx.search_deck_groups(
        [(_is_fighting_pokemon, 1, "Choose a Fighting Pokémon"),
         (_is_item, 1, "Choose an Item card")],
        prompt="Choose a Fighting Pokémon and an Item card")
    cards = [c for g in groups or [] for c in g]
    if cards:
        await ctx.put_in_hand(cards, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="0a884062-fb4e-5970-ba25-7ae0834d6dd3",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Korrina.Name",
    display_name="Korrina",
    searchable_by=["Korrina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    effect=korrina,
    condition=deck_nonempty
)
