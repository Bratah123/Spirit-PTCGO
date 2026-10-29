from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import spatial_control, hydro_pressure, zero_vanish_gx

card = PokemonCardDef(
    guid="477c978f-9c44-55c5-b1fd-9efe94bf478e",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaGX.Name",
    display_name="Palkia-GX",
    searchable_by=["Palkia-GX", "Basic", "GX", "PalkiaGX"],
    subtypes=["Basic", "GX"],
    collector_number=132,
    set_code="SM6",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=484,
    abilities=[
        Attack(
            title="Spatial Control",
            game_text="Move any number of Energy from your Benched Pok\u00e9mon to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=spatial_control,
        ),
        Attack(
            title="Hydro Pressure",
            game_text="This attack does 20 more damage times the amount of Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=hydro_pressure,
        ),
        Attack(
            title="Zero Vanish-GX",
            game_text="Shuffle all Energy from each of your opponent's Pok\u00e9mon into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=zero_vanish_gx,
        ),
    ],
)
