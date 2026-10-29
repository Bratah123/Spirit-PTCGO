from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.hf import psycrush_gx


card = PokemonCardDef(
    guid="8184e12f-0cb6-546e-a819-355e8346242c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusGX.Name",
    display_name="Tornadus-GX",
    searchable_by=["Tornadus-GX", "Basic", "GX", "TornadusGX"],
    subtypes=["Basic", "GX"],
    collector_number=134,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=641,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Wild Fury",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=30),
        ),
        Attack(
            title="Destructive Cyclone-GX",
            game_text="Discard all Energy from your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=psycrush_gx,
        ),
    ],
)