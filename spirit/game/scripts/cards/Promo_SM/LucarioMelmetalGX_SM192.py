from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm10 import (
    full_metal_wall_gx,
    steel_fist,
)

card = PokemonCardDef(
    guid="c747a7fc-45ef-5d79-9886-a23ed43f537b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioMelmetalGX.Name",
    display_name="Lucario & Melmetal-GX",
    searchable_by=["Lucario & Melmetal-GX", "Basic", "TAG TEAM", "GX", "LucarioMelmetalGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=192,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=448,
    abilities=[
        Attack(
            title="Steel Fist",
            game_text="Search your deck for a Metal Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=steel_fist
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
        ),
        Attack(
            title="Full Metal Wall-GX",
            game_text="For the rest of this game, your Metal Pok\u00e9mon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance). If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), discard all Energy from your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=full_metal_wall_gx
        ),
    ],
)