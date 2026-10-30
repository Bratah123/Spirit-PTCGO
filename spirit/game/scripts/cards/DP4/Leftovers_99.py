"""Leftovers (DP4 #99)."""
from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import leftovers_eot_heal

card = PokemonToolCardDef(
    guid="94540bcd-b129-552a-8c67-7f0f0116b303",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Leftovers.Name",
    display_name="Leftovers",
    searchable_by=["Leftovers", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=99,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Leftovers",
            game_text="If the Pokémon Leftovers is attached to is your Active Pokémon at the end of your turn, remove 1 damage counter from the Pokémon.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=leftovers_eot_heal(),
        ),
    ],
)
