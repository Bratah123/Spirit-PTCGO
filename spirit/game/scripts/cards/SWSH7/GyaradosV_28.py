from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a7b05098-4e2d-515f-b43f-2cdac25ffc09",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosV.Name",
    display_name="Gyarados V",
    searchable_by=["Gyarados V", "Basic", "V", "GyaradosV"],
    subtypes=["Basic", "V"],
    collector_number=28,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=130,
    abilities=[
        Attack(
            title="Get Angry",
            game_text="This attack does 20 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Storm",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)