from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import energy_root_passive

card = PokemonToolCardDef(
    guid="c3cebfb7-1434-535e-a670-7dcab2fc4d21",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRoot.Name",
    display_name="Energy Root",
    searchable_by=["Energy Root", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=83,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    passive=energy_root_passive(),
)
