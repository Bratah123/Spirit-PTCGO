from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench, is_basic

card = SupporterCardDef(
    guid="dc213941-179c-5ab2-92d1-a6fd6dac20b4",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pokémon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=9,
    set_code="POP4",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(
        is_basic, count=2,
        prompt="Choose up to 2 Basic Pokémon to put onto your Bench.",
    ),
)
