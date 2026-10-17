from spirit.game.data_utils import DeckBoxDef
from spirit.game.attributes import DefaultCosmetic, DeckBoxShape

product = DeckBoxDef(
    guid=DefaultCosmetic.DECK_BOX.value,
    key="NoSet",
    name="Basic Deck Box",
    image_url="_default_deckbox",
    shape=DeckBoxShape.TWO_TONE
)
