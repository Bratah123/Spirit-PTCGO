from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm8 import (
    burst_gx,
    mind_blown,
)

card = PokemonCardDef(
    guid="6da8c9b2-7e91-59af-a40d-7f20fc46d2b3",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlacephalonGX.Name",
    display_name="Blacephalon-GX",
    searchable_by=["Blacephalon-GX", "Basic", "GX", "Ultra Beast", "BlacephalonGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=52,
    set_code="SM8",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=806,
    abilities=[
        Attack(
            title="Bursting Burn",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Mind Blown",
            game_text="Put any amount of Fire Energy attached to your Pok\u00e9mon in the Lost Zone. This attack does 50 damage for each card put in the Lost Zone in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="x",
            effect=mind_blown
        ),
        Attack(
            title="Burst-GX",
            game_text="Discard 1 of your Prize cards. If it's an Energy card, attach it to 1 of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=burst_gx
        ),
    ],
)