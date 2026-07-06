from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53f2dbdb-bf15-5fbf-9852-14584b1d7983",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic", "Klink"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=599,
    abilities=[
        Attack(
            title="Call for Backup",
            game_text="Search your deck for a Metal Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
    ],
)