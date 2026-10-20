"""STUB: effect not implemented — do not guess mechanics.
Aromatisse (XY9 #85): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="245b3323-a1bd-5ad1-ade4-3381f325dd14",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name",
    display_name="Aromatisse",
    searchable_by=["Aromatisse", "Stage 1", "Aromatisse"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    family_id=682,
    abilities=[
        Attack(
            title="Dizzying Cologne",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)