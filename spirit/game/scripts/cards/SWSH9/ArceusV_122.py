from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba8e44a9-5efd-5592-ac85-f1f69a39ae5c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusV.Name",
    display_name="Arceus V",
    searchable_by=["Arceus V", "Basic", "V", "ArceusV"],
    subtypes=["Basic", "V"],
    collector_number=122,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Trinity Charge",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pok\u00e9mon V in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Power Edge",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)