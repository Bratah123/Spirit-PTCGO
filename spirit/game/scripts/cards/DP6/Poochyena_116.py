"""STUB: effect not implemented — do not guess mechanics.
Poochyena (DP6 #116): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import magma_ring_no_retreat
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="8f844a46-5c58-5d35-9747-ee8073ac8081",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    display_name="Poochyena",
    searchable_by=["Poochyena", "Basic", "Poochyena"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=261,
    abilities=[
        Attack(
            title="Corner",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=magma_ring_no_retreat(),
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)