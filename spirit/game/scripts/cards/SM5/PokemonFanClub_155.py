from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import pokemon_fan_club

card = SupporterCardDef(
    guid="2eea6736-f3b1-5c8f-abcc-8ee163897512",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=pokemon_fan_club,
)
