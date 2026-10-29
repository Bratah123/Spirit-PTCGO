from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import hydro_pressure, spatial_control, zero_vanish_gx

card = PokemonCardDef(
    guid="bbc59869-76c6-57c3-8aaf-97d7452582fd",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaGX.Name",
    display_name="Palkia-GX",
    searchable_by=["Palkia-GX", "Basic", "GX", "PalkiaGX"],
    subtypes=["Basic", "GX"],
    collector_number=147,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
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