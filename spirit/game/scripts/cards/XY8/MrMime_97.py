from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when, is_in_active_spot
from spirit.game.card_effects.attacks_common import flip_damage


def _bench_barrier(calc, carrier):
    """Prevent all damage done to your Benched Pokemon by attacks (either
    player's attacks)."""
    target = calc.target
    return bool(calc.is_attack and target is not None
                and target.owning_player_id == carrier.owning_player_id
                and not is_in_active_spot(target))


card = PokemonCardDef(
    guid="b7c88007-b26c-505b-bd9b-6880f3fb8047",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by attacks.",
            passive=prevent_damage_when(_bench_barrier, attacks_only=False),
        ),
        Attack(
            title="Juggling",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(4, per_heads=10),
        ),
    ],
)