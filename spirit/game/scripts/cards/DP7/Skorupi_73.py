"""STUB: effect not implemented — do not guess mechanics.
Skorupi (DP7 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import magma_ring_no_retreat


card = PokemonCardDef(
    guid="a078ef33-d74e-5f2b-ae68-a19388c3ded5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    display_name="Skorupi",
    searchable_by=["Skorupi", "Basic", "Skorupi"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=451,
    abilities=[
        Attack(
            title="Stalk",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=magma_ring_no_retreat(),
        ),
        Attack(
            title="Dangerous Claw",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)