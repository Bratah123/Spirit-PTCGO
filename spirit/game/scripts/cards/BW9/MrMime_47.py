from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import prevent_damage_when, is_in_active_spot


def _bench_barrier(calc, carrier):
    """Prevent all damage done to your Benched Pokemon by attacks (either
    player's attacks)."""
    target = calc.target
    return bool(calc.is_attack and target is not None
                and target.owning_player_id == carrier.owning_player_id
                and not is_in_active_spot(target))


card = PokemonCardDef(
    guid="7ebe9ee1-6e30-59f4-b858-4f0081b39373",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=prevent_damage_when(_bench_barrier, attacks_only=False),
        ),
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)