from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon


class StruggleGlovesPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not calc.attacker or not calc.to_active:
            return
        weak = holder.get_attribute(AttrID.WEAKNESS_TYPES) or []
        target_types = calc.target.get_attribute(AttrID.POKEMON_TYPES) or []
        if any(t in weak for t in target_types):
            calc.amount += 30


card = PokemonToolCardDef(
    guid="b9a1540c-e933-543d-a27a-653634e006c8",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StruggleGloves.Name",
    display_name="Struggle Gloves",
    searchable_by=["Struggle Gloves", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=171,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    passive=StruggleGlovesPassive(),
)
