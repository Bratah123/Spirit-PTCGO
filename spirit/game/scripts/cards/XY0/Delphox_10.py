"""STUB: effect not implemented — do not guess mechanics.
Delphox (XY0 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ebdbf050-4277-59f0-add2-f11c8bc3d572",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)