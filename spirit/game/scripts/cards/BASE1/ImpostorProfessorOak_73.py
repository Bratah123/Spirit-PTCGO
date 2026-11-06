from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import impostor_professor_oak

card = ItemCardDef(
    guid="e16799ba-3669-5cd4-85d3-19b374cb8623",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImpostorProfessorOak.Name",
    display_name="Impostor Professor Oak",
    searchable_by=["Impostor Professor Oak"],
    subtypes=[],
    collector_number=73,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=impostor_professor_oak,
)
