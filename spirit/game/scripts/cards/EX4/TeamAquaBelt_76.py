from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import attach_to_team, team_belt_between_turns

_GUID = "cd2fc041-274c-5f40-bbbb-df945207e758"

card = PokemonToolCardDef(
    guid="cd2fc041-274c-5f40-bbbb-df945207e758",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaBelt.Name",
    display_name="Team Aqua Belt",
    searchable_by=["Team Aqua Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=76,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_team("Team Aqua"),
    granted_abilities=[
        Ability(
            title="Team Aqua Belt",
            game_text="At any time between turns, if the Pokémon Team Aqua Belt is attached to is your Active Pokémon, search your deck for a card that evolves from that Pokémon and put it on that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward, then discard Team Aqua Belt.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=team_belt_between_turns(_GUID),
        ),
    ],
)
