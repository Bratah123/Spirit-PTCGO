"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Rhyhorn (EX4 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ex import second_strike


card = PokemonCardDef(
    guid="9f5fce90-e22c-5e30-8b49-0fb8f2ade2f0",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasRhyhorn.Name",
    display_name="Team Magma's Rhyhorn",
    searchable_by=["Team Magma's Rhyhorn", "Basic", "TeamMagmasRhyhorn"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=111,
    abilities=[
        Attack(
            title="Double Stab",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Second Strike",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=second_strike(10, 20, 2),
        ),
    ],
)