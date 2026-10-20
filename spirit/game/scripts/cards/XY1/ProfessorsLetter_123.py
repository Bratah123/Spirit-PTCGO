from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="21203d92-01e2-5ef5-98a5-e62266cc3807",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsLetter.Name",
    display_name="Professor's Letter",
    searchable_by=["Professor's Letter", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_energy_card, count=2, minimum=0, reveal=True,
                           prompt='Choose up to 2 basic Energy cards'),
    condition=deck_nonempty
)
