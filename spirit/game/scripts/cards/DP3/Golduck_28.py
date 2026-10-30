"""STUB: effect not implemented — do not guess mechanics.
Golduck (DP3 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5456e493-c481-5343-83b8-690b89c4f146",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Encore",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can use only that attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Break Beam",
            game_text="You may do 40 damage plus 20 more damage. If you do, Golduck is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)