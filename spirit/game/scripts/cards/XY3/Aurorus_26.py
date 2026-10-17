"""STUB: effect not implemented — do not guess mechanics.
Aurorus (XY3 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5069d292-7a44-5005-9e92-d9ea4e5e66ad",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name",
    display_name="Aurorus",
    searchable_by=["Aurorus", "Stage 1", "Aurorus"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    family_id=698,
    abilities=[
        Ability(
            title="Ice Shield",
            game_text="Any damage done by an opponent's attack to each of your Water Pok\u00e9mon that has any Water Energy attached to it is reduced by 20 (after applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)