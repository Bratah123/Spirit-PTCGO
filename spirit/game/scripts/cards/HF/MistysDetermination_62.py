from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.hf import mistys_determination
from spirit.game.card_effects.trainers import hand_size_at_least

card = SupporterCardDef(
    guid="493e7048-1e85-5b6d-8959-f0dcb579bb85",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDetermination.Name",
    display_name="Misty's Determination",
    searchable_by=["Misty's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=62,
    set_code="HF",
    rarity=Rarities.Uncommon,
    effect=mistys_determination,
    condition=hand_size_at_least(2),
)
