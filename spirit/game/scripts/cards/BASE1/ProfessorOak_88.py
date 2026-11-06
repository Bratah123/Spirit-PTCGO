from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professors_research
from spirit.game.card_effects.ecard import has_cards_in_deck


card = ItemCardDef(
    guid="ae3252b8-e1cc-5290-9385-a1d6b276ac79",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOak.Name",
    display_name="Professor Oak",
    searchable_by=["Professor Oak"],
    subtypes=[],
    collector_number=88,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=professors_research,
)
