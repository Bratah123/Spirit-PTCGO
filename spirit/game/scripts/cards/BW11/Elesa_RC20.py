from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType
from spirit.game.card_effects.support_common import search_to_hand


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value


_elesa = search_to_hand(_is_tool, count=3, reveal=True, prompt="Choose up to 3 Pokémon Tool cards")

card = SupporterCardDef(
    guid="15aac43c-a084-596e-b0ec-0c846f138b1d",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Elesa.Name",
    display_name="Elesa",
    searchable_by=["Elesa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="BW11",
    rarity=Rarities.Common,
    effect=_elesa
)
