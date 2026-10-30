from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    rockets_sneak_attack_condition,
    team_rockets_evil_deeds,
)


card = ItemCardDef(
    guid="ff17bf31-7963-5204-9aeb-caae73a94664",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsEvilDeeds.Name",
    display_name="Team Rocket's Evil Deeds",
    searchable_by=["Team Rocket's Evil Deeds"],
    subtypes=[],
    collector_number=103,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    condition=rockets_sneak_attack_condition,
    effect=team_rockets_evil_deeds,
)
