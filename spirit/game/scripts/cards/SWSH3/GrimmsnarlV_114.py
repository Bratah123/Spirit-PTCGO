from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f880c265-6c9a-52ea-8769-b64edcddd9e9",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name",
    display_name="Grimmsnarl V",
    searchable_by=["Grimmsnarl V", "Basic", "V", "GrimmsnarlV"],
    subtypes=["Basic", "V"],
    collector_number=114,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=861,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Spiky Knuckle",
            game_text="Put 2 Darkness Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)