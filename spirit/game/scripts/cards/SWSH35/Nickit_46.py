from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ef9e2c5-2103-5449-83ed-c06b2637bd2b",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    display_name="Nickit",
    searchable_by=["Nickit", "Basic", "Nickit"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SWSH35",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=827,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)