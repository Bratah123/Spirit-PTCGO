from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_tower_passive


card = StadiumCardDef(
    guid="ba7b44d7-1844-5afb-8ea6-57337372144a",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonTower.Name",
    display_name="Pokémon Tower",
    searchable_by=["Pok\u00e9mon Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=42,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    passive=pokemon_tower_passive,
)
