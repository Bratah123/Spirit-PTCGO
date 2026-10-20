from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.passives import carrier_pokemon


def _holder(pokemon, carrier):
    """The Pokemon this card is attached to has no Retreat Cost."""
    return pokemon is carrier_pokemon(carrier)


card = PokemonToolCardDef(
    guid="fdf34d23-7b49-586c-bd51-14cab081eb27",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloatStone.Name",
    display_name="Float Stone",
    searchable_by=["Float Stone", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    passive=retreat_free_when(_holder)
)
