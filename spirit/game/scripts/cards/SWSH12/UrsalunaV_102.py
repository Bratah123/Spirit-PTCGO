from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3fc8d7a1-d601-5b59-9dac-3e8e196f790c",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UrsalunaV.Name",
    display_name="Ursaluna V",
    searchable_by=["Ursaluna V", "Basic", "V", "UrsalunaV"],
    subtypes=["Basic", "V"],
    collector_number=102,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=901,
    abilities=[
        Ability(
            title="Hard Coat",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Peat Shoulder",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)