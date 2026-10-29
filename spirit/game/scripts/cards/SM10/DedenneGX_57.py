from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    dedechange,
    tingly_return_gx,
)

card = PokemonCardDef(
    guid="f3ddc3fc-cba3-5b83-af3b-6784927a8848",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DedenneGX.Name",
    display_name="Dedenne-GX",
    searchable_by=["Dedenne-GX", "Basic", "GX", "DedenneGX"],
    subtypes=["Basic", "GX"],
    collector_number=57,
    set_code="SM10",
    rarity=Rarities.RareHoloGX,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Ability(
            title="Dedechange",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard your hand and draw 6 cards. You can't use more than 1 Dedechange Ability each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            shared_once_per_turn="Dedechange",
            effect=dedechange
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Tingly Return-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. Put this Pok\u00e9mon and all cards attached to it into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=tingly_return_gx
        ),
    ],
)