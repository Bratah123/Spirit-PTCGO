from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="434562c9-a907-5b12-8734-6327f6b24d2a",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    display_name="Milcery",
    searchable_by=["Milcery", "Basic", "Milcery"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=868,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)