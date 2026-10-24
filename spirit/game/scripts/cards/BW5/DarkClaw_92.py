from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon, effective_pokemon_types


class DarkClawPassive(Passive):
    """Holder is a Darkness Pok\u00e9mon: its attacks do +20 to the opponent's
    Active (before Weakness and Resistance)."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker:
            return
        if PokemonTypes.DARKNESS.value in effective_pokemon_types(calc.board, holder):
            calc.amount += 20


card = PokemonToolCardDef(
    guid="b0c9b3c9-9d9d-55ef-9c08-630e46ecdb3f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkClaw.Name",
    display_name="Dark Claw",
    searchable_by=["Dark Claw", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    passive=DarkClawPassive()
)
