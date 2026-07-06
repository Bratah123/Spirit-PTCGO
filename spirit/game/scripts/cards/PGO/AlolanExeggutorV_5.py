from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="010594a7-0853-5833-933f-009a6aea83f6",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorV.Name",
    display_name="Alolan Exeggutor V",
    searchable_by=["Alolan Exeggutor V", "Basic", "V", "AlolanExeggutorV"],
    subtypes=["Basic", "V"],
    collector_number=5,
    set_code="PGO",
    rarity=Rarities.RareHoloV,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=103,
    abilities=[
        Attack(
            title="Growing Tall",
            game_text="Flip a coin. If heads, search your deck for up to 5 Grass Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Head Swing",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each Grass Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)