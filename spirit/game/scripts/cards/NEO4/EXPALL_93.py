from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import exp_all


card = PokemonToolCardDef(
    guid="d9d5a4d1-738d-5b47-81de-9e3e2e52e3bc",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EXPALL.Name",
    display_name="EXP.ALL",
    searchable_by=["EXP.ALL", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=93,
    set_code="NEO4",
    rarity=Rarities.Rare,
    granted_abilities=[
        Ability(
            title="EXP.ALL",
            game_text="During your opponent's turn, if your Active Pok\u00e9mon would be Knocked Out by your opponent's attack, you may take 1 of the basic Energy cards attached to your Active Pok\u00e9mon and attach it to the Pok\u00e9mon with EXP.ALL attached to it. If you do, discard EXP.ALL.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=exp_all,
        ),
    ],
)
