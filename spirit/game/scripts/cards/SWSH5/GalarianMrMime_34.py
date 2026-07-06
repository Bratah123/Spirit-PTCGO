from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4382431-e15b-5c1f-b644-a3680efb5669",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    display_name="Galarian Mr. Mime",
    searchable_by=["Galarian Mr. Mime", "Basic", "GalarianMrMime"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=122,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Find It",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)