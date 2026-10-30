from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import erikas_maids, erikas_maids_condition


card = ItemCardDef(
    guid="113c011b-e436-551c-ae53-2dac3cff60c7",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasMaids.Name",
    display_name="Erika's Maids",
    searchable_by=["Erika's Maids"],
    subtypes=[],
    collector_number=109,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    condition=erikas_maids_condition,
    effect=erikas_maids,
)
