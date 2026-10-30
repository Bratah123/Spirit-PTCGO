from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import focus_band_passive


card = PokemonToolCardDef(
    guid="eb76395f-e6b4-54b2-b5f9-052d16fa9b94",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FocusBand.Name",
    display_name="Focus Band",
    searchable_by=["Focus Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=86,
    set_code="NEO1",
    rarity=Rarities.Rare,
    passive=focus_band_passive,
)
