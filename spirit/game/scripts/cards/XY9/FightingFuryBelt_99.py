from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonStage
from spirit.game.session.passives import Passive, carrier_pokemon


class _FightingFuryBelt(Passive):
    """The Basic Pokemon this is attached to gets +40 HP and its attacks do 10
    more to the opponent's Active (before W/R)."""
    def _basic(self, pokemon, carrier):
        me = carrier_pokemon(carrier)
        return me is not None and pokemon is me and me.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value

    def max_hp_bonus(self, pokemon, carrier):
        return 40 if self._basic(pokemon, carrier) else 0

    def modify_damage_dealt(self, calc, carrier):
        if calc.attacker is not None and calc.is_attack and calc.is_opposing and calc.to_active \
                and self._basic(calc.attacker, carrier):
            calc.amount += 10


card = PokemonToolCardDef(
    guid="a1bc0828-b71f-596d-8e12-a06ef6ba2838",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingFuryBelt.Name",
    display_name="Fighting Fury Belt",
    searchable_by=["Fighting Fury Belt", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=99,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    passive=_FightingFuryBelt()
)
