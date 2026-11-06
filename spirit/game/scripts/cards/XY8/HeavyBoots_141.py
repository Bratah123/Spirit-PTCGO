from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID, SpecialConditions
from spirit.game.session.passives import Passive, carrier_pokemon


class _HeavyBoots(Passive):
    """If the holder's Retreat Cost is 3 or more: +20 HP and it can't be Confused."""
    def _heavy(self, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if me is None or pokemon is not me:
            return False
        # Printed Retreat Cost (the HP/condition hooks get no board for the
        # live, passive-adjusted cost).
        return int(me.get_attribute(AttrID.RETREAT_COST) or 0) >= 3

    def max_hp_bonus(self, pokemon, carrier):
        return 20 if self._heavy(pokemon, carrier) else 0

    def blocks_special_conditions(self, target, condition, carrier):
        return condition == SpecialConditions.CONFUSED and self._heavy(target, carrier)


card = PokemonToolCardDef(
    guid="45cfde93-0bea-5428-b2b2-cc8af213e333",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBoots.Name",
    display_name="Heavy Boots",
    searchable_by=["Heavy Boots", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=141,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=_HeavyBoots()
)
