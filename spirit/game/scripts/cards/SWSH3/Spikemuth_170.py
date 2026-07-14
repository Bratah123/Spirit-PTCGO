from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class _SpikemuthPassive(Passive):
    """Whenever a player's Active Pokemon moves to the Bench during their
    turn, put 2 damage counters on that Pokemon."""

    def counters_on_active_to_bench(self, pokemon, carrier):
        return 2


card = StadiumCardDef(
    guid="d9d948bc-f256-5705-b541-ba076c9cb68f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Spikemuth.Name",
    display_name="Spikemuth",
    searchable_by=["Spikemuth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=170,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    passive=_SpikemuthPassive(),
)
