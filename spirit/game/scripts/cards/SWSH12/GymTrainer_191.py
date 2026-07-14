from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import conditional_draw

gym_trainer = conditional_draw(2, 2, lambda ctx: bool(ctx.kos_suffered_last_turn()))

card = SupporterCardDef(
    guid="98a19d72-4605-5821-b9cb-cd6b2d1e82b4",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymTrainer.Name",
    display_name="Gym Trainer",
    searchable_by=["Gym Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=191,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    effect=gym_trainer
)
