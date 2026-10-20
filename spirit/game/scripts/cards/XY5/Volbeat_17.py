"""STUB: effect not implemented — do not guess mechanics.
Volbeat (XY5 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="c0bb20c9-daf2-564a-b549-813788b015ce",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
        Attack(
            title="Pester",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)