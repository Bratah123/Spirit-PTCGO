"""STUB: effect not implemented — do not guess mechanics.
Trapinch (EX12 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, flip_damage


card = PokemonCardDef(
    guid="ad2e5923-3761-547b-9395-48c95e53260b",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch",
    searchable_by=["Trapinch", "Basic", "Trapinch"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title="Pebble Throw",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(10, also_base=True),
        ),
        Attack(
            title="Double Pinchers",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)