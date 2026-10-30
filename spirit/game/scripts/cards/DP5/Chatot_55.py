"""STUB: effect not implemented — do not guess mechanics.
Chatot (DP5 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import mime_draw_equal_opponent
from spirit.game.card_effects.ex import magma_ring_no_retreat


card = PokemonCardDef(
    guid="024693b1-71c4-5857-bd8d-46a89f0ce5b4",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Chatot"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=441,
    abilities=[
        Attack(
            title="Mimic",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={},
            # STUB: attack effect not implemented
            effect=mime_draw_equal_opponent(),
        ),
        Attack(
            title="Chatter",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=magma_ring_no_retreat(),
        ),
    ],
)