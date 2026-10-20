"""STUB: effect not implemented — do not guess mechanics.
Pelipper (XY6 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b4def2fe-2474-5be5-8fb7-a299c70a6ef6",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper",
    searchable_by=["Pelipper", "Stage 1", "Pelipper"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=278,
    abilities=[
        Attack(
            title="Swallow",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)