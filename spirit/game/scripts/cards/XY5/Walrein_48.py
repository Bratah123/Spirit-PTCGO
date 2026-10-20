"""STUB: effect not implemented — do not guess mechanics.
Walrein (XY5 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="10e4a00a-9da2-568d-8e31-32e726ea148a",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2", "Walrein"],
    subtypes=["Stage 2"],
    collector_number=48,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Frozen Splash",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 70 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)