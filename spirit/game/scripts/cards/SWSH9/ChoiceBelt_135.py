from spirit.game.card_effects.pokemon import ChoiceBeltPassive
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a4309622-34a1-5398-9237-091ad3bc0acd",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBelt.Name",
    display_name="Choice Belt",
    searchable_by=["Choice Belt", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=135,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    passive=ChoiceBeltPassive()
)
