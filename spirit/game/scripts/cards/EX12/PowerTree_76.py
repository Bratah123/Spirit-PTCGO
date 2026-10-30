"""EX12 Legend Maker — Power Tree stadium.
"""
from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.ex import power_tree_effect


card = StadiumCardDef(
    guid="062a4d57-2b14-50d6-a998-4207aa9cd370",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerTree.Name",
    display_name="Power Tree",
    searchable_by=["Power Tree", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Power Tree",
        game_text="Once during each player's turn, if the player has no Special Energy cards in his or her discard pile, that player searches his or her discard pile for a basic Energy card, show it to the opponent, and put it into his or her hand.",
        ability_type=AbilityTypes.POKE_POWER,
        effect=power_tree_effect(),
        activation=Activations.ONCE_PER_TURN,
    ),
)
