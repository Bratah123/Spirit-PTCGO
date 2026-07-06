from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e657b7fe-75a8-50c7-85ed-6423f7d04aa2",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitanV.Name",
    display_name="Galarian Darmanitan V",
    searchable_by=["Galarian Darmanitan V", "Basic", "V", "GalarianDarmanitanV"],
    subtypes=["Basic", "V"],
    collector_number=169,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=555,
    abilities=[
        Attack(
            title="Freezing Headbutt",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Frozen Slice",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
    ],
)