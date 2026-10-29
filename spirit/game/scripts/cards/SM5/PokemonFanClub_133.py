from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import pokemon_fan_club

card = SupporterCardDef(
    guid="ff12d892-5b1d-5aca-a2a3-2a0039a4c3fc",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=pokemon_fan_club,
)
