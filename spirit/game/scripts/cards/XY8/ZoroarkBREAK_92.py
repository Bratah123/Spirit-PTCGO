"""STUB: effect not implemented — do not guess mechanics.
Zoroark BREAK (XY8 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="de2cdf48-d739-5183-b3fd-2ee9c600fb56",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZoroarkBREAK.Name",
    display_name="Zoroark BREAK",
    searchable_by=["Zoroark BREAK", "BREAK", "ZoroarkBREAK"],
    subtypes=["BREAK"],
    collector_number=92,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Foul Play",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)