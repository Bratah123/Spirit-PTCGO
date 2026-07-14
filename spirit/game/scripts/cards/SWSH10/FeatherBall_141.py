from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand


def _no_retreat_pokemon(card):
    return is_pokemon_card(card) and int(card.get_attribute(AttrID.RETREAT_COST) or 0) == 0


card = ItemCardDef(
    guid="5e68504e-3c22-568d-8dcf-81449c97f37a",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FeatherBall.Name",
    display_name="Feather Ball",
    searchable_by=["Feather Ball", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _no_retreat_pokemon, count=1, minimum=0, reveal=True,
        prompt="Choose a Pokémon that has no Retreat Cost.",
    ),
)
