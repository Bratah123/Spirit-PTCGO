from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon


class _RustedSwordPassive(Passive):
    """+30 damage to the opponent's Active from the attached Zacian V."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if (
            calc.is_attack
            and calc.is_opposing
            and calc.to_active
            and holder is calc.attacker
            and holder.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "ZacianV"
        ):
            calc.amount += 30


card = PokemonToolCardDef(
    guid="4a0e1002-2542-58e5-83e6-9281a0ccf4e8",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RustedSword.Name",
    display_name="Rusted Sword",
    searchable_by=["Rusted Sword", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=62,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    passive=_RustedSwordPassive(),
)
