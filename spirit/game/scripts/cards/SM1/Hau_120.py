from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="f471107c-e923-58bd-830c-34517922bfad",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3),
    condition=deck_nonempty
)
