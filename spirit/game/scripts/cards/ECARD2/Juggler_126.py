from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import juggler, juggler_condition


card = SupporterCardDef(
    guid="7c18debc-aa03-5c09-bcbc-d2590b55bd96",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Juggler.Name",
    display_name="Juggler",
    searchable_by=["Juggler", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    condition=juggler_condition,
    effect=juggler,
)
