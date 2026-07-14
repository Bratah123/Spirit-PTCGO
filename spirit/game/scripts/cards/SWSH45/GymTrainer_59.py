from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import conditional_draw

gym_trainer = conditional_draw(2, 2, lambda ctx: bool(ctx.kos_suffered_last_turn()))

card = SupporterCardDef(
    guid="ec1ef86f-165b-5355-b53f-fdb557866c26",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymTrainer.Name",
    display_name="Gym Trainer",
    searchable_by=["Gym Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    effect=gym_trainer
)
