from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import ancient_ruins, ancient_ruins_condition


card = StadiumCardDef(
    guid="ab4d0d31-b831-544a-a999-cc68262693ca",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientRuins.Name",
    display_name="Ancient Ruins",
    searchable_by=["Ancient Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=119,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Ancient Ruins",
        game_text="Once during each player's turn (before he or she attacks), if he or she has not played a Supporter card, that player may reveal his or her hand to his or her opponent. If that player reveals his or her hand and there is no Supporter card there, that player draws a card.",
        activation=Activations.ONCE_PER_TURN,
        condition=ancient_ruins_condition,
        effect=ancient_ruins,
    ),
)
