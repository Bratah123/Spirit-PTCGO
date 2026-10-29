from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm8 import (
    dream_fear_gx,
    lets_snuggle,
)

card = PokemonCardDef(
    guid="72d188e6-41d7-552d-b6c9-e901d3ba03ee",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuGX.Name",
    display_name="Mimikyu-GX",
    searchable_by=["Mimikyu-GX", "Basic", "GX", "MimikyuGX"],
    subtypes=["Basic", "GX"],
    collector_number=149,
    set_code="SM8",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Let's Snuggle & Fall",
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=lets_snuggle
        ),
        Attack(
            title="Dream Fear-GX",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. Your opponent shuffles that Pok\u00e9mon and all cards attached to it into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            effect=dream_fear_gx
        ),
    ],
)