from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import the_rockets_trap


card = ItemCardDef(
    guid="1edcdd0e-f7ce-5a0d-8e37-2d7fc33d7699",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheRocketsTrap.Name",
    display_name="The Rocket's Trap",
    searchable_by=["The Rocket's Trap"],
    subtypes=[],
    collector_number=19,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    effect=the_rockets_trap,
)
