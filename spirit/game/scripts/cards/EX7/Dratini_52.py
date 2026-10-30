from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72f45265-025b-5973-9225-ea9b3da3a852",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=147,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)