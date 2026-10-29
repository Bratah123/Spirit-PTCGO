from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.attributes import AttrID


from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot


def _own_benched(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    parent = getattr(target, "parent", None)
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"


class DauntingPosePassive(Passive):
    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        return _own_benched(calc.target, carrier)

    def prevents_damage_counters(self, target, carrier, source_player_id=None):
        if source_player_id == carrier.owning_player_id:
            return False
        return _own_benched(target, carrier)


card = PokemonCardDef(
    guid="bccb0b1b-2f13-530b-b07b-3fbbf6d17fb5",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Daunting Pose",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks. Your opponent's attacks and Abilities can't put damage counters on your Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=DauntingPosePassive(),
            effect=None,
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)