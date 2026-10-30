"""STUB: effect not implemented — do not guess mechanics.
Banette (DP3 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="465cd453-e8a2-50f4-b8f6-37058e252e46",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Ghost Head",
            game_text="Put as many damage counters as you like on Banette. (You can't put more than Banette's remaining HP.) Put that many damage counters on the Defending Pok\u00e9mon.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spiteful Pain",
            game_text="If Banette is in your discard pile, this attack does 40 damage plus 40 more damage, then search your discard pile for Banette, show it to your opponent, and shuffle it into your deck.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)