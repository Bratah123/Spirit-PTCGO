from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card

card = SupporterCardDef(
    guid="2308f25f-baff-599f-8cec-169cf0244c7d",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokKid.Name",
    display_name="PokÃ© Kid",
    searchable_by=["Pok\u00c3\u00a9 Kid", "Supporter"],
    subtypes=["Supporter"],
    collector_number=70,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(
        is_pokemon_card, count=1, minimum=0, reveal=True,
        prompt="Choose a Pokémon to put into your hand.",
    )
)
