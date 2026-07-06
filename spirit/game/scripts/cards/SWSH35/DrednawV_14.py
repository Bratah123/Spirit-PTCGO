from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d251cfb-4b45-5d50-8608-945478d94d2c",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrednawV.Name",
    display_name="Drednaw V",
    searchable_by=["Drednaw V", "Basic", "V", "DrednawV"],
    subtypes=["Basic", "V"],
    collector_number=14,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=834,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Powerful Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)