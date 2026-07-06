from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ea3cc7e-dc72-567f-a12e-2ef2022247c8",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlappleV.Name",
    display_name="Flapple V",
    searchable_by=["Flapple V", "Basic", "V", "FlappleV"],
    subtypes=["Basic", "V"],
    collector_number=143,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=841,
    abilities=[
        Attack(
            title="Sour Spit",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost ColorlessColorless more.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)