from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import massive_catch_gx, school_storm

card = PokemonCardDef(
    guid="bb2b48f4-178e-5efd-8aee-5981dca87f8f",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WishiwashiGX.Name",
    display_name="Wishiwashi-GX",
    searchable_by=["Wishiwashi-GX", "Basic", "GX", "WishiwashiGX"],
    subtypes=["Basic", "GX"],
    collector_number=63,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Attack(
            title="School Storm",
            game_text="This attack does 20 damage for each of your Wishiwashi and Wishiwashi-GX in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=school_storm,
        ),
        Attack(
            title="Massive Catch-GX",
            game_text="Look at the top 12 cards of your deck and put any number of Basic Pok\u00e9mon you find there onto your Bench. Shuffle the other cards back into your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=massive_catch_gx,
        ),
    ],
)