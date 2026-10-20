"""STUB: effect not implemented — do not guess mechanics.
Gastrodon (XY11 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="46531862-b540-5974-ad37-a1e93d0f849c",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastrodon.Name",
    display_name="Gastrodon",
    searchable_by=["Gastrodon", "Stage 1", "Gastrodon"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    family_id=422,
    abilities=[
        Attack(
            title="Sticky Shot",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)