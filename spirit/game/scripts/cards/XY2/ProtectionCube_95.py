from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon


def _own_attack_on_holder(calc, carrier):
    """Damage the holder's own attacks do to it (recoil)."""
    holder = carrier_pokemon(carrier)
    return calc.is_attack and calc.target is holder and calc.attacker is holder


card = PokemonToolCardDef(
    guid="460abd81-5454-5c75-9c5b-c6e4abc88cf3",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProtectionCube.Name",
    display_name="Protection Cube",
    searchable_by=["Protection Cube", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    passive=prevent_damage_when(_own_attack_on_holder, attacks_only=False)
)
