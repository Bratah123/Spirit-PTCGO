from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import center_lady_playable, pokemon_center_lady

card = SupporterCardDef(
    guid="c814e210-ce04-5c6d-9099-12f80c5a0112",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCenterLady.Name",
    display_name="Pokémon Center Lady",
    searchable_by=["Pok\u00e9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="HF",
    rarity=Rarities.Uncommon,
    effect=pokemon_center_lady,
    condition=center_lady_playable,
)
