from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand

from spirit.game.card_effects.sm9 import (
    devilish_hands_gx,
)

card = PokemonCardDef(
    guid="6f696557-513d-50de-a317-db6e3bae8921",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaGX.Name",
    display_name="Hoopa-GX",
    searchable_by=["Hoopa-GX", "Basic", "GX", "HoopaGX"],
    subtypes=["Basic", "GX"],
    collector_number=96,
    set_code="SM9",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=720,
    abilities=[
        Attack(
            title="Rogue Ring",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=search_to_hand(count=2),
        ),
        Attack(
            title="Dark Strike",
            game_text="This Pok\u00e9mon can't use Dark Strike during your next turn.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=160,
            locks_next_turn=True,
        ),
        Attack(
            title="Devilish Hands-GX",
            game_text="Choose 1 of your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX 6 times. (You can choose the same Pok\u00e9mon more than once.) For each time you chose a Pok\u00e9mon, do 30 damage to it. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 3},
            effect=devilish_hands_gx,
        ),
    ],
)