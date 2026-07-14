from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot, team_damage_boost_passive
from spirit.game.card_effects.pokemon import is_pokemon_gx
from spirit.game.card_effects.attacks_common import snipe_attack


def _is_rapid_strike(pokemon):
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


def _throwing_coach_target(target):
    if is_in_active_spot(target):
        return False
    return is_pokemon_v(target.archetype_id) or is_pokemon_gx(target.archetype_id)


card = PokemonCardDef(
    guid="c95b8198-79d9-5bfe-a39e-d15512be5632",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic", "Rapid Strike", "Passimian"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=88,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Ability(
            title="Throwing Coach",
            game_text="Your Rapid Strike Pok\u00e9mon's attacks do 30 more damage to your opponent's Benched Pok\u00e9mon V and Benched Pok\u00e9mon-GX (before applying Weakness and Resistance). You can't apply more than 1 Throwing Coach Ability at a time.",
            passive=team_damage_boost_passive(
                30, attacker_pred=_is_rapid_strike, target_pred=_throwing_coach_target,
                once_key="ThrowingCoach", to_active_only=False,
            ),
        ),
        Attack(
            title="Fling",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=snipe_attack(20, pool="any", count=1),
        ),
    ],
)