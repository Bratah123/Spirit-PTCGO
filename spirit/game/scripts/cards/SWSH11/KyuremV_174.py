from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b410b0d-266f-5392-9b8c-c5e1a3a7d92b",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremV.Name",
    display_name="Kyurem V",
    searchable_by=["Kyurem V", "Basic", "V", "KyuremV"],
    subtypes=["Basic", "V"],
    collector_number=174,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Rapid Freeze",
            game_text="Attach any number of Water Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 3},
            damage=140,
        ),
    ],
)