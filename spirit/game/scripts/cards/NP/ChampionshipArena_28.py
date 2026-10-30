from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import championship_arena_end_turn


card = StadiumCardDef(
    guid="9ee1eb42-ac0d-5d23-b89d-4af5ae9b6022",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionshipArena.Name",
    display_name="Championship Arena",
    searchable_by=["Championship Arena", "Stadium"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="NP",
    rarity=Rarities.RarePromo,
    abilities=[
        Ability(
            title="Championship Arena",
            game_text="At the end of each player's turn, if that player has 8 or more cards in his or her hand, that player discards a number of cards until that player has 7 cards left in his or her hand.",
            trigger=Triggers.END_OF_TURN,
            effect=championship_arena_end_turn,
        ),
    ],
)
