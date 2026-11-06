from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    sabrinas_esp, sabrinas_esp_condition, sabrinas_esp_passive,
    sabrinas_esp_targets,
)


card = ItemCardDef(
    guid="f466c6f3-4782-52c0-b0c3-aa3b1963e120",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasESP.Name",
    display_name="Sabrina's ESP",
    searchable_by=["Sabrina's ESP"],
    subtypes=[],
    collector_number=117,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    condition=sabrinas_esp_condition,
    effect=sabrinas_esp,
    play_targets=sabrinas_esp_targets,
    play_target_prompt="Choose a Pokémon with Sabrina in its name",
)
card.passive = sabrinas_esp_passive
