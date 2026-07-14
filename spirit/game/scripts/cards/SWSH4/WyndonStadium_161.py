from spirit.game.data_utils import StadiumCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class _WyndonStadiumPassive(Passive):
    """Whenever either player plays a Pokemon VMAX from their hand to evolve
    a Pokemon V during their turn, heal 100 damage from that Pokemon."""

    def heal_on_evolve(self, evolved, pre_evolution, player_id, carrier):
        if "VMAX" not in subtypes_for(evolved.archetype_id):
            return 0
        if "V" not in subtypes_for(pre_evolution.archetype_id):
            return 0
        return 100


card = StadiumCardDef(
    guid="b2e2dcc5-2de2-5a8c-98b1-bca51266cad4",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WyndonStadium.Name",
    display_name="Wyndon Stadium",
    searchable_by=["Wyndon Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=161,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    passive=_WyndonStadiumPassive(),
)
