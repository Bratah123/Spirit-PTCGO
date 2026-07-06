from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cd2388b-cff7-5c31-82f0-3518bced8c4f",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianElectrodeV.Name",
    display_name="Hisuian Electrode V",
    searchable_by=["Hisuian Electrode V", "Basic", "V", "HisuianElectrodeV"],
    subtypes=["Basic", "V"],
    collector_number=172,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=101,
    abilities=[
        Attack(
            title="Tantrum Blast",
            game_text="This attack does 100 damage for each Special Condition affecting this Pok\u00e9mon.",
            cost={},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Solar Shot",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)