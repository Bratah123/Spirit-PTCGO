from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_special_energy


class _AssaultVest(Passive):
    """Damage from attacks by opposing Pokemon with any Special Energy attached
    is reduced by 40 (after Weakness and Resistance)."""
    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        att = calc.attacker
        if (me is None or calc.target is not me or not calc.is_attack or att is None
                or att.owning_player_id == me.owning_player_id):
            return
        if any(is_special_energy(e) for e in calc.board.attached_energies(att)):
            calc.amount = max(0, calc.amount - 40)


card = PokemonToolCardDef(
    guid="f54a3999-16b8-5b65-abd8-76ea5df7846f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AssaultVest.Name",
    display_name="Assault Vest",
    searchable_by=["Assault Vest", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=133,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=_AssaultVest()
)
