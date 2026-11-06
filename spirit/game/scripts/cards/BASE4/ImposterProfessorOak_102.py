from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import impostor_professor_oak


card = ItemCardDef(
    guid="801f371c-6e63-56bf-beb9-32e261154a44",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImposterProfessorOak.Name",
    display_name="Imposter Professor Oak",
    searchable_by=["Imposter Professor Oak"],
    subtypes=[],
    collector_number=102,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=impostor_professor_oak,
)
