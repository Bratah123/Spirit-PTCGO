from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.passives import carrier_pokemon


def _holder(pokemon, carrier):
    """The Pokemon this card is attached to has no Retreat Cost."""
    return pokemon is carrier_pokemon(carrier)


card = PokemonToolCardDef(
    guid="5d073628-31df-5dd0-91f1-df851a226be7",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloatStone.Name",
    display_name="Float Stone",
    searchable_by=["Float Stone", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=137,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=retreat_free_when(_holder)
)
