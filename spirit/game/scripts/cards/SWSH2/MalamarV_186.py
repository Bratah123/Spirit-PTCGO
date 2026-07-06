from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4fd160f-b8e6-58f5-8dc2-a12ee60523ee",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MalamarV.Name",
    display_name="Malamar V",
    searchable_by=["Malamar V", "Basic", "V", "MalamarV"],
    subtypes=["Basic", "V"],
    collector_number=186,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=687,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. This attack does 30 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Brain Shake",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)