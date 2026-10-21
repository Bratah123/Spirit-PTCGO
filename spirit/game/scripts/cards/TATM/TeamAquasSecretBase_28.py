from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import Passive


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


class _SecretBase(Passive):
    """The Retreat Cost of each Pokemon in play (except Team Aqua Pokemon) is Colorless more."""
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        return cost if _team(pokemon, "Aqua") else cost + 1


card = StadiumCardDef(
    guid="b153aa0a-2aa0-5609-b220-9f77233a7231",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasSecretBase.Name",
    display_name="Team Aqua's Secret Base",
    searchable_by=["Team Aqua's Secret Base", "Stadium"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    passive=_SecretBase()
)
