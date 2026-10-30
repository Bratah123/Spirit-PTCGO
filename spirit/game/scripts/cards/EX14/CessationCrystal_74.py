from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import cessation_crystal_passive

card = PokemonToolCardDef(
    guid="bb431f97-354d-50ef-861f-38d9c248a1e2",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CessationCrystal.Name",
    display_name="Cessation Crystal",
    searchable_by=["Cessation Crystal", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=74,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=cessation_crystal_passive(),
)
