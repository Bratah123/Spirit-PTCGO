from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fbbf3bd2-581e-5037-9a5c-eb3e24e41a38",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniEX.Name",
    display_name="Victini-EX",
    searchable_by=["Victini-EX", "Basic", "EX", "VictiniEX"],
    subtypes=["Basic", "EX"],
    collector_number=24,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Turbo Energize",
            game_text="Search your deck for 2 basic Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Intensifying Burn",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 50 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)