from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sl import pokemon_breeder
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="4ab16c4a-4239-5ad8-8502-ea6bd5f0215f",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="SL",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=pokemon_breeder,
)
