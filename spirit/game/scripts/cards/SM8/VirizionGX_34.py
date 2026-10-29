from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack

from spirit.game.card_effects.sm8 import (
    breeze_away_gx,
    sensitive_blade,
)

card = PokemonCardDef(
    guid="40ef41fc-5f75-5868-9b58-ed8271a02bbd",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionGX.Name",
    display_name="Virizion-GX",
    searchable_by=["Virizion-GX", "Basic", "GX", "VirizionGX"],
    subtypes=["Basic", "GX"],
    collector_number=34,
    set_code="SM8",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Attack(
            title="Double Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Sensitive Blade",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator="+",
            effect=sensitive_blade
        ),
        Attack(
            title="Breeze Away-GX",
            game_text="Put any number of your Pok\u00e9mon in play and all cards attached to them into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=breeze_away_gx
        ),
    ],
)