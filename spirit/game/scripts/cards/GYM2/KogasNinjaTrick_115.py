from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    kogas_ninja_trick,
    kogas_ninja_trick_condition,
    kogas_ninja_trick_passive,
    kogas_ninja_trick_targets,
)


card = ItemCardDef(
    guid="cc0e79bc-ef4e-591c-9415-1ac7730a6802",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasNinjaTrick.Name",
    display_name="Koga's Ninja Trick",
    searchable_by=["Koga's Ninja Trick"],
    subtypes=[],
    collector_number=115,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    condition=kogas_ninja_trick_condition,
    effect=kogas_ninja_trick,
    play_targets=kogas_ninja_trick_targets,
    play_target_prompt="Choose a Pokémon with Koga in its name",
)
card.passive = kogas_ninja_trick_passive
