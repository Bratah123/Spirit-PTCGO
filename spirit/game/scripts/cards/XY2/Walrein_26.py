"""STUB: effect not implemented — do not guess mechanics.
Walrein (XY2 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea548117-c5e1-54d4-96e1-280fe1b8c87f",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2", "Walrein"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="XY2",
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
            title="Powder Snow",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Big Tusk",
            game_text="This attack does 120 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)