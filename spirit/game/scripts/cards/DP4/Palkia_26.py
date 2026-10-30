"""DP4 Great Encounters — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import search_to_hand
from spirit.game.card_effects.dp import spacial_rend
from spirit.game.card_effects.dp import transback

card = PokemonCardDef(
    guid="5de586b4-51c8-5ddc-87ca-bb9feeb9b5f7",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic", "Palkia"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="DP4",
    rarity=Rarities.Rare,
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
            effect=spacial_rend(),
        ),
        Attack(
            title="Transback",
            game_text="You may flip a coin. If heads, discard all Energy attached to Palkia and put the Defending Pok\u00e9mon and all cards attached to it on top of your opponent's deck. Your opponent shuffles his or her deck afterward.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=transback(),
        ),
    ],
)