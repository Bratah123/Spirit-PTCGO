from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.trainers import is_v_or_gx


class TelescopicSightPassive(Passive):
    """The holder's attacks do +30 to the opponent's Benched Pokemon V/GX."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.attacker:
            return
        if calc.to_active:
            return
        if is_v_or_gx(calc.target.archetype_id):
            calc.amount += 30


card = PokemonToolCardDef(
    guid="a4225101-ea08-598f-9213-31cf21195a45",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TelescopicSight.Name",
    display_name="Telescopic Sight",
    searchable_by=["Telescopic Sight", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=160,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    passive=TelescopicSightPassive(),
)
