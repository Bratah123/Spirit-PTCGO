"""EX12 Legend Maker — Full Flame stadium.
"""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import full_flame_passive


card = StadiumCardDef(
    guid="1abc2770-40e4-51f1-8771-3bb5b86b271d",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullFlame.Name",
    display_name="Full Flame",
    searchable_by=["Full Flame", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    passive=full_flame_passive(),
)
