from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import curse_powder_passive

card = PokemonToolCardDef(
    guid="0348afb2-4d7c-5ab4-bcb8-1d9b7c130515",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursePowder.Name",
    display_name="Curse Powder",
    searchable_by=["Curse Powder", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=80,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    passive=curse_powder_passive(),
)
