"""Bubble Coat (DP6 #129)."""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import bubble_coat_passive

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
)
