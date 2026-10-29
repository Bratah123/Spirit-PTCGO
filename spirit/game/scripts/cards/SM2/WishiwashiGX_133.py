from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.scripts.cards.SM2.WishiwashiGX_38 import blue_surge_gx


card = PokemonCardDef(
    guid="240c2a6d-f025-54ca-b3df-e441e667e7b0",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WishiwashiGX.Name",
    display_name="Wishiwashi-GX",
    searchable_by=["Wishiwashi-GX", "Basic", "GX", "WishiwashiGX"],
    subtypes=["Basic", "GX"],
    collector_number=133,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Torrential Vortex",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Blue Surge-GX",
            game_text="Move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=blue_surge_gx,
        ),
    ],
)