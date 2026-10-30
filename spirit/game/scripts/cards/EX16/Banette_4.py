"""STUB: effect not implemented — do not guess mechanics.
Banette (EX16 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import bench_manipulation, grudge_damage
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ff64e15b-a54d-53bc-8d93-59dcacdca09f",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Grudge",
            game_text="Does 20 damage plus 10 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=grudge_damage(20, 10),
        ),
        Attack(
            title="Bench Manipulation",
            game_text="Your opponent flips a number of coins equal to the number of his or her Benched Pok\u00e9mon. This attack does 40 damage times the number of tails. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=bench_manipulation(),
        ),
    ],
)