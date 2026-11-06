from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professors_research
from spirit.game.card_effects.ecard import has_cards_in_deck


card = ItemCardDef(
    guid="2843a9a2-e8a6-5563-bbdb-368206b29ae9",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOak.Name",
    display_name="Professor Oak",
    searchable_by=["Professor Oak"],
    subtypes=[],
    collector_number=116,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=professors_research,
)
