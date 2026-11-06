from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.passives import Passive
from spirit.game.content.definitions import def_for


class _FightingStadium(Passive):
    """Each Fighting Pokemon's attacks (both players) do 20 more damage to
    the Defending Pokemon-EX (before W/R)."""
    def modify_damage_dealt(self, calc, carrier):
        a, t = calc.attacker, calc.target
        if not (calc.is_attack and calc.is_opposing and calc.to_active and a and t):
            return
        if PokemonTypes.FIGHTING.value not in (a.get_attribute(AttrID.POKEMON_TYPES) or []):
            return
        if "EX" in (getattr(def_for(t.archetype_id), "subtypes", None) or []):
            calc.amount += 20


card = StadiumCardDef(
    guid="d32c8e6b-3a8f-5b02-a431-15c3145fa013",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingStadium.Name",
    display_name="Fighting Stadium",
    searchable_by=["Fighting Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=_FightingStadium()
)
