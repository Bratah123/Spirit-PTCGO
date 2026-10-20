"""STUB: effect not implemented — do not guess mechanics.
Magmar (XY12 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd2e6441-8873-58e4-9111-5440466fffd3",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Fire Punch",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)