"""STUB: effect not implemented — do not guess mechanics.
Lugia BREAK (XY10 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="68fbb567-1a34-5469-97cc-6cd11c4370cb",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaBREAK.Name",
    display_name="Lugia BREAK",
    searchable_by=["Lugia BREAK", "BREAK", "LugiaBREAK"],
    subtypes=["BREAK"],
    collector_number=79,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    family_id=249,
    abilities=[
        Attack(
            title="Flash of Destruction",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)