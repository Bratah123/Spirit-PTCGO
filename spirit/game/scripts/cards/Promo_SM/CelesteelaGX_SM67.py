from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import blaster_gx, rocket_fall

card = PokemonCardDef(
    guid="49e5c794-4f64-595f-956e-82db76856427",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelesteelaGX.Name",
    display_name="Celesteela-GX",
    searchable_by=["Celesteela-GX", "Basic", "GX", "Ultra Beast", "CelesteelaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=67,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=797,
    abilities=[
        Attack(
            title="Rocket Fall",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=rocket_fall,
        ),
        Attack(
            title="Moon Press",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
        Attack(
            title="Blaster-GX",
            game_text="Turn all of your Prize cards face up. (Those Prize cards remain face up for the rest of the game.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=blaster_gx,
        ),
    ],
)