from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_bench_space, search_to_bench


card = SupporterCardDef(
    guid="7799c6ef-fa02-552d-8547-50e3be4db7b0",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    condition=requires_bench_space(1),
    effect=search_to_bench(
        count=2,
        prompt="Choose up to 2 Baby Pokémon and/or Basic Pokémon cards to put onto your Bench.",
    ),
)
