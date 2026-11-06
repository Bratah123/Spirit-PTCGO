from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class _HexManiac(Passive):
    """Each Pokemon has no Abilities."""
    def blocks_abilities(self, pokemon, carrier):
        return True


async def hex_maniac(ctx):
    """Until the end of your opponent's next turn, each Pokemon in play, in
    each player's hand, and in each player's discard pile has no Abilities."""
    ctx.add_global_passive(_HexManiac(), ctx.session.turn_state.turn_number + 1)


card = SupporterCardDef(
    guid="8c046ff9-96ec-516b-a2d1-d3a865757bdb",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HexManiac.Name",
    display_name="Hex Maniac",
    searchable_by=["Hex Maniac", "Supporter"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    effect=hex_maniac
)
