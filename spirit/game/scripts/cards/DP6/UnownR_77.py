"""STUB: effect not implemented — do not guess mechanics.
Unown [R] (DP6 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="cee5d918-476c-5532-9d1b-6ce1d06de7ac",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownR.Name",
    display_name="Unown [R]",
    searchable_by=["Unown [R]", "Basic", "UnownR"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="RETIRE",
            game_text="Once during your turn, if Unown R is on your Bench, you may discard Unown R and all cards attached to it. (This doesn't count as a Knocked Out Pok\u00e9mon.) Then, draw a card.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Move any number of basic Energy cards attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)