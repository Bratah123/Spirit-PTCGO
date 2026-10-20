"""STUB: effect not implemented — do not guess mechanics.
Boldore (XY4 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d082fc28-b792-5ada-90c7-8bb2219fccd1",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    display_name="Boldore",
    searchable_by=["Boldore", "Stage 1", "Boldore"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Core Heal",
            game_text="Discard a Fighting Energy attached to this Pok\u00e9mon and heal 50 damage from it.",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 3},
            damage=60,
        ),
    ],
)