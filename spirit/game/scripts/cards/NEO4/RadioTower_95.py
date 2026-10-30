from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import radio_tower, radio_tower_condition


card = StadiumCardDef(
    guid="895f22af-3f5c-50da-96c1-2dcf5ad8327e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RadioTower.Name",
    display_name="Radio Tower",
    searchable_by=["Radio Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=95,
    set_code="NEO4",
    rarity=Rarities.Rare,
    ability=Ability(
        title="Radio Tower",
        game_text="Once during each player's turn (before attacking), that player may look at the top 2 cards of his or her deck and put them back in the same order.",
        activation=Activations.ONCE_PER_TURN,
        condition=radio_tower_condition,
        effect=radio_tower,
    ),
)
