from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when


def _to_bench(calc, carrier):
    """Any attack damage to a Benched Pokemon (both players)."""
    return calc.is_attack and calc.target is not None and not calc.to_active


card = StadiumCardDef(
    guid="c6c72ca5-6e31-5b00-a99d-cee00ca1c061",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MountainRing.Name",
    display_name="Mountain Ring",
    searchable_by=["Mountain Ring", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=prevent_damage_when(_to_bench, attacks_only=False)
)
