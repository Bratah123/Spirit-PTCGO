from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import looker_whistle

card = ItemCardDef(
    guid="be2917bb-9f22-5f45-9c31-37495b84cc06",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LookerWhistle.Name",
    display_name="Looker Whistle",
    searchable_by=["Looker Whistle", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=looker_whistle,
)
