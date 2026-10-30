"""STUB: effect not implemented — do not guess mechanics.
Palkia (DPP #DP27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ced0e32d-617a-5be8-babf-43b1913b3696",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic", "Palkia"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Attack(
            title="Spacial Rend",
            game_text="Search your deck for a Stadium card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. If there is any Stadium card in play, discard it.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Transback",
            game_text="You may flip a coin. If heads, discard all Energy attached to Palkia and put the Defending Pok\u00e9mon and all cards attached to it on top of your opponent's deck. Your opponent shuffles his or her deck afterward.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)