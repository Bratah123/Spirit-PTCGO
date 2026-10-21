from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _WideLens(Passive):
    """Damage from this Pokemon's attacks is affected by Weakness and
    Resistance for your opponent's Benched Pokemon."""
    def modify_damage_dealt(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing and not calc.to_active
                and carrier_pokemon(carrier) is calc.attacker):
            calc.apply_modifiers = True


card = PokemonToolCardDef(
    guid="3fc2f08d-eca4-5445-917f-671123b7bfda",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WideLens.Name",
    display_name="Wide Lens",
    searchable_by=["Wide Lens", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=_WideLens()
)
