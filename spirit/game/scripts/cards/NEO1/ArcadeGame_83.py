from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import arcade_game, has_cards_in_deck


card = ItemCardDef(
    guid="cd37f2ff-8a76-5d83-bb71-24844fa471aa",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArcadeGame.Name",
    display_name="Arcade Game",
    searchable_by=["Arcade Game", "Goldenrod Game Corner"],
    subtypes=["Goldenrod Game Corner"],
    collector_number=83,
    set_code="NEO1",
    rarity=Rarities.Rare,
    condition=has_cards_in_deck,
    effect=arcade_game,
)
