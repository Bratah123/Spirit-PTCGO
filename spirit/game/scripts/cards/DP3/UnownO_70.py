"""STUB: effect not implemented — do not guess mechanics.
Unown [O] (DP3 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="bd2e8b92-89f9-5e23-a7b6-0a789ace4113",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownO.Name",
    display_name="Unown [O]",
    searchable_by=["Unown [O]", "Basic", "UnownO"],
    subtypes=["Basic"],
    collector_number=70,
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
            title="ONE",
            game_text="Once during your turn (before your attack), if you have Unown O, Unown N, and Unown E on your Bench and you have 1 card left in your hand, you may draw cards until you have 7 cards in your hand.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)