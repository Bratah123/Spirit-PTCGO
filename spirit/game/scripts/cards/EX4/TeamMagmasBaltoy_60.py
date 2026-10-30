"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Baltoy (EX4 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="272bf5c0-1088-50bf-88eb-e45a7d9d8bac",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    display_name="Team Magma's Baltoy",
    searchable_by=["Team Magma's Baltoy", "Basic", "TeamMagmasBaltoy"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=343,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)