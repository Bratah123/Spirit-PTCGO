from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import lucky_stadium, lucky_stadium_condition


card = StadiumCardDef(
    guid="53558e57-a4d1-5d49-bf3f-af31b2fa8a88",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyStadium.Name",
    display_name="Lucky Stadium",
    searchable_by=["Lucky Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=100,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Lucky Stadium",
        game_text="Once during each player's turn (before attacking), that player may flip a coin. If heads, that player draws a card.",
        activation=Activations.ONCE_PER_TURN,
        condition=lucky_stadium_condition,
        effect=lucky_stadium,
    ),
)
