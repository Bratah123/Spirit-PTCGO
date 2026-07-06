from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d7be742-d405-5c3c-befb-5ef93a4db3ea",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaticate.Name",
    display_name="Alolan Raticate",
    searchable_by=["Alolan Raticate", "Stage 1", "AlolanRaticate"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Chase Up",
            game_text="Search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Super Fang",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)