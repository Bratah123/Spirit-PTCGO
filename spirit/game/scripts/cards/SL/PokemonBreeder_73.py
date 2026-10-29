from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sl import pokemon_breeder
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="e3d53a72-4e15-5199-a727-57e92c8346ba",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="SL",
    rarity=Rarities.RareUltra,
    condition=deck_nonempty,
    effect=pokemon_breeder,
)
