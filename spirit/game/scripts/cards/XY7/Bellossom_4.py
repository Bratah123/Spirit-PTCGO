"""STUB: effect not implemented — do not guess mechanics.
Bellossom (XY7 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5dca825b-872d-52e4-b840-ce040e058afc",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name",
    display_name="Bellossom",
    searchable_by=["Bellossom", "Stage 2", "Bellossom"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Windmill",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flower Tornado",
            game_text="Move as many Grass Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)