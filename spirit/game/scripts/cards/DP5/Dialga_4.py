"""STUB: effect not implemented — do not guess mechanics.
Dialga (DP5 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_until_effect


card = PokemonCardDef(
    guid="381d20db-7fdb-5a63-ac5f-86c2b0d9ae38",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title="Time Shift",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Diamond Blast",
            game_text="Flip a coin. If heads, this attack does 60 damage plus 20 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)