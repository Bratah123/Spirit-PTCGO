from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26ed2e00-0d24-5cf3-8aa3-b9447e3d4987",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=610,
    abilities=[
        Attack(
            title="Strong Bond",
            game_text="Search your deck for a Supporter card named Iris, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)