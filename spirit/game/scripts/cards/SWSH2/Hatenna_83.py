from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83145193-6021-55e0-9d41-809b5610341e",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    display_name="Hatenna",
    searchable_by=["Hatenna", "Basic", "Hatenna"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=856,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)