from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import is_in_active_spot


class GalarMinePassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if is_in_active_spot(pokemon):
            return cost + 2
        return cost


card = StadiumCardDef(
    guid="8f6486b5-b50d-51cc-9b8f-fc469e8a02b7",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GalarMine.Name",
    display_name="Galar Mine",
    searchable_by=["Galar Mine", "Stadium"],
    subtypes=["Stadium"],
    collector_number=160,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    passive=GalarMinePassive()
)
