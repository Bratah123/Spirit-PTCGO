from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="2cbda0aa-4cf8-523d-80f3-3e5f2417a63c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pok\u00e9mon Fan Club",
    searchable_by=["Pokémon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_pokemon, count=2, minimum=0, reveal=True,
                           prompt='Choose up to 2 Basic Pokémon'),
    condition=deck_nonempty
)
