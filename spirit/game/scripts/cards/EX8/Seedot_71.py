"""STUB: effect not implemented — do not guess mechanics.
Seedot (EX8 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="da686dd2-c149-5c5f-aee6-7b2ffb7580d2",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    display_name="Seedot",
    searchable_by=["Seedot", "Basic", "Seedot"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=273,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=draw_attack(1),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)