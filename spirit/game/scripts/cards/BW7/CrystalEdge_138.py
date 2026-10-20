from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_named(pokemon, name):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and d.display_name == name


class CrystalEdgePassive(Passive):
    """ACE SPEC: attached to White Kyurem-EX, each of its attacks does 50 more
    damage to the opponent's Active (before Weakness and Resistance)."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if (holder is not None and calc.attacker is holder and calc.is_attack
                and calc.is_opposing and calc.to_active and calc.amount > 0
                and _is_named(holder, "White Kyurem-EX")):
            calc.amount += 50


card = PokemonToolCardDef(
    guid="72d126ec-bc95-5c63-a4ee-2094d119d97a",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalEdge.Name",
    display_name="Crystal Edge",
    searchable_by=["Crystal Edge", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=138,
    set_code="BW7",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    passive=CrystalEdgePassive()
)
