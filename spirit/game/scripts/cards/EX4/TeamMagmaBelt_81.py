from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import attach_to_team, team_belt_between_turns

_GUID = "d7e857d0-9148-532f-8e60-72576f99906e"

card = PokemonToolCardDef(
    guid="d7e857d0-9148-532f-8e60-72576f99906e",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaBelt.Name",
    display_name="Team Magma Belt",
    searchable_by=["Team Magma Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=81,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_team("Team Magma"),
    granted_abilities=[
        Ability(
            title="Team Magma Belt",
            game_text="At any time between turns, if the Pokémon Team Magma Belt is attached to is your Active Pokémon, search your deck for a card that evolves from that Pokémon and put it on that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward, then discard Team Magma Belt.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=team_belt_between_turns(_GUID),
        ),
    ],
)
