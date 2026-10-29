"""STUB: effect not implemented — do not guess mechanics.
Shining Volcanion (SL #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, flip_damage


card = PokemonCardDef(
    guid="e7d1f0b9-2455-5704-8b87-5e5a2afd1399",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningVolcanion.Name",
    display_name="Shining Volcanion",
    searchable_by=["Shining Volcanion", "Basic", "ShiningVolcanion"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SL",
    rarity=Rarities.Shining,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=721,
    abilities=[
        Attack(
            title="Dual Pump",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            # STUB: attack effect not implemented
            effect=snipe_attack(50, pool='any', count=2),
        ),
        Attack(
            title="Quad Smash",
            game_text="Flip 4 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=4, per_heads=50),
        ),
    ],
)