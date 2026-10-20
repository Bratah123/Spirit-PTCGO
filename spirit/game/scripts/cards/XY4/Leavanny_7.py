"""STUB: effect not implemented — do not guess mechanics.
Leavanny (XY4 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f005164e-f0fc-5ddc-8674-9d138ffced25",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny", "Stage 2", "Leavanny"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Coordinate",
            game_text="Choose up to 2 of your Benched Pok\u00e9mon that have no Pok\u00e9mon Tools attached to them. For each of those Pok\u00e9mon, search your deck for a Pok\u00e9mon Tool card, and attach it to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Storm",
            game_text="Heal 20 damage from each of your Grass Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)