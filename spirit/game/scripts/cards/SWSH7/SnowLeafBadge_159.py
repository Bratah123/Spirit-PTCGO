from spirit.game.data_utils import PokemonToolCardDef, is_pokemon_v, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


def _eligible(pokemon):
    if pokemon is None or not is_pokemon_v(pokemon.archetype_id):
        return False
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", None) or ""
    return "Leafeon" in name or "Glaceon" in name


class SnowLeafBadgePassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if pokemon is holder and _eligible(holder):
            return 0
        return cost

    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if calc.target is holder and _eligible(holder):
            calc.weakness_applies = False


card = PokemonToolCardDef(
    guid="e4183947-34e2-5c63-b9d5-d37826e82012",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SnowLeafBadge.Name",
    display_name="Snow Leaf Badge",
    searchable_by=["Snow Leaf Badge", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=159,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    passive=SnowLeafBadgePassive(),
)
