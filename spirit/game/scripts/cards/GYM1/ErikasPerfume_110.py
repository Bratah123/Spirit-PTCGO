from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import erikas_perfume


card = ItemCardDef(
    guid="c4c84d52-9fdd-59ae-bfc5-f6d4dce6972e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasPerfume.Name",
    display_name="Erika's Perfume",
    searchable_by=["Erika's Perfume"],
    subtypes=[],
    collector_number=110,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=erikas_perfume,
)
