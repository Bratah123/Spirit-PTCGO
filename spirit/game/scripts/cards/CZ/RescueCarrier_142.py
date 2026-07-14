from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard


def _low_hp_pokemon(card):
    return is_pokemon_card(card) and (card.get_attribute(AttrID.HP, 999) or 0) <= 90


card = ItemCardDef(
    guid="0205ee20-a659-547a-9f16-f0eb96fe47d6",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueCarrier.Name",
    display_name="Rescue Carrier",
    searchable_by=["Rescue Carrier", "Item"],
    subtypes=["Item"],
    collector_number=142,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(
        _low_hp_pokemon, count=2, reveal=False,
        prompt="Put up to 2 Pokémon with 90 HP or less from your discard pile into your hand",
    ),
    condition=requires_discard(_low_hp_pokemon),
)
