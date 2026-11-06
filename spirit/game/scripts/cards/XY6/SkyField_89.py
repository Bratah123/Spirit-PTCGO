from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class _SkyField(Passive):
    """Each player can have 8 Pokemon on his or her Bench (the engine's
    bench-capacity enforcement discards the excess when this leaves play)."""
    def bench_capacity(self, player_id, carrier):
        return 8


card = StadiumCardDef(
    guid="81f06034-e5c6-5c67-b544-9600c2591bfe",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyField.Name",
    display_name="Sky Field",
    searchable_by=["Sky Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=_SkyField()
)
