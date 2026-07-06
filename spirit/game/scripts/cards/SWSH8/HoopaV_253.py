from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="05bc0901-d9ea-5491-81eb-e1db95f4837a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaV.Name",
    display_name="Hoopa V",
    searchable_by=["Hoopa V", "Basic", "V", "Fusion Strike", "HoopaV"],
    subtypes=["Basic", "V", "Fusion Strike"],
    collector_number=253,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=720,
    abilities=[
        Ability(
            title="Two-Faced",
            game_text="As long as this Pok\u00e9mon is in play, it is Psychic and Darkness type.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Impact",
            game_text="Put 3 damage counters on 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)