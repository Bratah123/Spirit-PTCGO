"""STUB: effect not implemented — do not guess mechanics.
Starmie BREAK (XY12 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f919691-ad5d-5128-8541-83e036a17016",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StarmieBREAK.Name",
    display_name="Starmie BREAK",
    searchable_by=["Starmie BREAK", "BREAK", "StarmieBREAK"],
    subtypes=["BREAK"],
    collector_number=32,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Break Star",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon BREAK. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)