from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


def _hp_90_or_less(card):
    return is_pokemon_card(card) and (card.get_attribute(AttrID.HP) or 0) <= 90


card = ItemCardDef(
    guid="d8ae26a2-67fb-5124-a882-4eadb99df02c",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LevelBall.Name",
    display_name="Level Ball",
    searchable_by=["Level Ball", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _hp_90_or_less, count=1,
        prompt="Choose a Pokémon with 90 HP or less to put into your hand.",
    )
)
