from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import pokemon_retriever

card = ItemCardDef(
    guid="c2824a97-1f80-5265-9046-a88d3763f435",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonRetriever.Name",
    display_name="Pokémon Retriever",
    searchable_by=["Pokémon Retriever", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=84,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=pokemon_retriever,
)
