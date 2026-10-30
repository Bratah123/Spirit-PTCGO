"""EXP. ALL: attach restriction + ON_ALLY_KNOCKED_OUT energy move."""
from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import attach_to_non_ex_non_owner, exp_all_on_ally_ko

card = PokemonToolCardDef(
    guid="89b46eb3-469d-54ba-9b84-154d808a71c6",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EXPALL.Name",
    display_name="EXP.ALL",
    searchable_by=["EXP. ALL", "EXP ALL", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=91,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_non_ex_non_owner(),
    granted_abilities=[
        Ability(
            title="EXP. ALL",
            game_text="During your opponent's turn, if 1 of your Active Pokémon is Knocked Out by your opponent's attack, you may take 1 basic Energy card attached to that Knocked Out Pokémon and attach it to the Pokémon with EXP.ALL attached to it. If you do, discard EXP.ALL.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=exp_all_on_ally_ko,
        ),
    ],
)
