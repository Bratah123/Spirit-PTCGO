"""STUB: effect not implemented — do not guess mechanics.
Unown [X] (DP3 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b338ecd6-5241-51ef-a7d7-52135c760fc7",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownX.Name",
    display_name="Unown [X]",
    searchable_by=["Unown [X]", "Basic", "UnownX"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="X-RAY",
            game_text="Once during your turn (before your attack), if you have Unown X on your Bench, you may look at the top card of your opponent's deck and put it back on top of his or her deck.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)