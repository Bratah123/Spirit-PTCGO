from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card

card = SupporterCardDef(
    guid="bece6b76-81de-5a5a-873a-4681fe181172",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokKid.Name",
    display_name="PokÃ© Kid",
    searchable_by=["Pok\u00c3\u00a9 Kid", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_pokemon_card, count=1, minimum=0, reveal=True,
        prompt="Choose a Pokémon to put into your hand.",
    )
)
