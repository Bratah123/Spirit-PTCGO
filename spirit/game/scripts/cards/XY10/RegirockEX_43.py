"""STUB: effect not implemented — do not guess mechanics.
Regirock-EX (XY10 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="987c3c8f-41ee-55b1-b887-1f5817c04335",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegirockEX.Name",
    display_name="Regirock-EX",
    searchable_by=["Regirock-EX", "Basic", "EX", "RegirockEX"],
    subtypes=["Basic", "EX"],
    collector_number=43,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Ability(
            title="Regi Power",
            game_text="The attacks of your Fighting Pok\u00e9mon (excluding Regirock-EX) do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bedrock Press",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)