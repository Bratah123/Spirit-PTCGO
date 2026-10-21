from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability


class _RoboBody(FossilBodyPassive):
    """Can't retreat; if Knocked Out, your opponent takes no Prize cards."""
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        return 0 if pokemon is carrier else count


card = FossilItemCardDef(
    guid="8457bcad-af76-541d-a184-e2d862a64b72",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoboSubstituteTeamFlareGear.Name",
    display_name="Robo Substitute Team Flare Gear",
    searchable_by=["Robo Substitute Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=30,
    passive=_RoboBody(),
    abilities=[fossil_discard_ability()]
)
