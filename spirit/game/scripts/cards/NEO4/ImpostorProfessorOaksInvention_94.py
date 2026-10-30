from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import impostor_oaks_invention


card = ItemCardDef(
    guid="ebfbca4d-594e-54a6-a20b-6a47a335c9e9",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImpostorProfessorOaksInvention.Name",
    display_name="Impostor Professor Oak's Invention",
    searchable_by=["Impostor Professor Oak's Invention"],
    subtypes=[],
    collector_number=94,
    set_code="NEO4",
    rarity=Rarities.Rare,
    effect=impostor_oaks_invention,
)
