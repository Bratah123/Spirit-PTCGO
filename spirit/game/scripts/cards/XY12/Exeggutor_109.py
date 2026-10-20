"""STUB: effect not implemented — do not guess mechanics.
ナッシー[Exeggutor] (XY12 #109): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8bcd190f-c582-5574-b079-f2a1a62192c4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="\u30ca\u30c3\u30b7\u30fc[Exeggutor]",
    searchable_by=["ナッシー[Exeggutor]", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=103,
    abilities=[
        Attack(
            title="\u3075\u307f\u3064\u3051[Stomp]",
            game_text="\u30b3\u30a4\u30f3\u30921\u56de\u6295\u3052\u30aa\u30e2\u30c6\u306a\u3089\u300110\u30c0\u30e1\u30fc\u30b8\u3092\u8ffd\u52a0\u3002 Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)