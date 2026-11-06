from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


class SilverBanglePassive(Passive):
    """The holder's attacks (excluding Pokemon-EX) do 30 more damage to Active
    Pokemon-EX (before W/R)."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if (calc.is_attack and calc.is_opposing and calc.attacker is holder
                and holder is not None and not _is_pokemon_ex(holder)
                and calc.to_active and _is_pokemon_ex(calc.target)):
            calc.amount += 30


card = PokemonToolCardDef(
    guid="174a5d56-e1c1-5c76-bc16-1c72752c6bba",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilverBangle.Name",
    display_name="Silver Bangle",
    searchable_by=["Silver Bangle", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=88,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    passive=SilverBanglePassive()
)
