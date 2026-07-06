from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b3fed0c-1fd8-5576-83ad-7ced9a5ef5b7",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    display_name="Galarian Mr. Mime",
    searchable_by=["Galarian Mr. Mime", "Basic", "GalarianMrMime"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=122,
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Triple Spin",
            game_text="Flip 3 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)