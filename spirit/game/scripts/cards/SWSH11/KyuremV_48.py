from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31832006-11a2-53d0-a709-a3bf0bcefa20",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremV.Name",
    display_name="Kyurem V",
    searchable_by=["Kyurem V", "Basic", "V", "KyuremV"],
    subtypes=["Basic", "V"],
    collector_number=48,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
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