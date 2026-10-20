"""STUB: effect not implemented — do not guess mechanics.
Exploud (XY10 #82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="92bb50ab-605d-5c2c-a3c4-5c63908f059f",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2", "Exploud"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(40),
        ),
        Attack(
            title="Cacophony",
            game_text="At the end of your opponent's next turn, discard the Defending Pok\u00e9mon and all cards attached to it.",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)