"""STUB: effect not implemented — do not guess mechanics.
Dialga (DPP #DP49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="06a557f9-bb96-53e5-a7a6-d609c237518a",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title="Time Call",
            game_text="Search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it onto that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Time Wager",
            game_text="Flip 2 coins. If either of them is tails, this attack's base damage is 50 instead of 100.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)