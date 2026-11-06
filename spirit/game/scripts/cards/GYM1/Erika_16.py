from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import erika


card = ItemCardDef(
    guid="c3978618-8737-5605-94d5-e09c82e3f262",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika"],
    subtypes=[],
    collector_number=16,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    effect=erika,
)
