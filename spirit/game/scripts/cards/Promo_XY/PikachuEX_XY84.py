"""STUB: effect not implemented — do not guess mechanics.
Pikachu-EX (Promo_XY #XY84): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="c8d3348f-6acc-51a2-a039-04ec2a651617",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuEX.Name",
    display_name="Pikachu-EX",
    searchable_by=["Pikachu-EX", "Basic", "EX", "PikachuEX"],
    subtypes=["Basic", "EX"],
    collector_number=84,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(until_tails=True, per_heads=30),
        ),
        Attack(
            title="Overspark",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)