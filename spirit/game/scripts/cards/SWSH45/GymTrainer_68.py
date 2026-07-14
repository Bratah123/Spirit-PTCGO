from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import conditional_draw

gym_trainer = conditional_draw(2, 2, lambda ctx: bool(ctx.kos_suffered_last_turn()))

card = SupporterCardDef(
    guid="99df5e28-f9fa-5326-a077-508539873816",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymTrainer.Name",
    display_name="Gym Trainer",
    searchable_by=["Gym Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=68,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=gym_trainer
)
