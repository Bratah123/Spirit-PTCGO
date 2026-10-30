"""Bubble Coat (DP6 #129)."""
from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import bubble_coat_passive, bubble_coat_discard_between_turns

card = PokemonToolCardDef(
    guid="44f3496a-7286-530d-b131-a494f9bc8393",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BubbleCoat.Name",
    display_name="Bubble Coat",
    searchable_by=["Bubble Coat", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=129,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    passive=bubble_coat_passive(),
    granted_abilities=[
        Ability(
            title="Bubble Coat",
            game_text="If that Pokémon is damaged by an opponent's attack, discard this card at the end of the turn.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=bubble_coat_discard_between_turns,
        ),
    ],
)
