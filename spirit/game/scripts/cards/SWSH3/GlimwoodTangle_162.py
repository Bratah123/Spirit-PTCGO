from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class _GlimwoodTanglePassive(Passive):
    """Once during each player's turn, after that player flips any coins for
    an attack, they may ignore all results and begin flipping again."""

    def offers_attack_coin_reroll(self, player_id, carrier):
        return True


card = StadiumCardDef(
    guid="4d910b75-6845-5f9b-99b1-e6b12b65af27",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlimwoodTangle.Name",
    display_name="Glimwood Tangle",
    searchable_by=["Glimwood Tangle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=162,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    passive=_GlimwoodTanglePassive(),
)
