from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23257b47-73e4-59a4-b9f1-6b69d84fe0d8",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    display_name="Stufful",
    searchable_by=["Stufful", "Basic", "Stufful"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=759,
    abilities=[
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)