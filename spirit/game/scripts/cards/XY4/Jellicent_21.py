"""STUB: effect not implemented — do not guess mechanics.
Jellicent (XY4 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="acad5162-543c-5d4d-91ce-af0a3ad00fb1",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent", "Stage 1", "Jellicent"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Attack(
            title="Meddling",
            game_text="Attach 3 Energy cards from your opponent's discard pile to his or her Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ensnaring Spray",
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)