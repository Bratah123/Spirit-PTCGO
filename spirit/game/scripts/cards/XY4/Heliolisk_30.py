"""STUB: effect not implemented — do not guess mechanics.
Heliolisk (XY4 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cfa7d0a2-4c25-5e81-9f0a-3b6c9381ef6e",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1", "Heliolisk"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Parabolic Spark",
            game_text="Discard as many Lightning Energy attached to your Pok\u00e9mon as you like. This attack does 30 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)