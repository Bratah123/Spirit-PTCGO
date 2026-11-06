from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7f32e87b-0838-5dd1-8461-f8c0e0a972c4",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    display_name="Ferroseed",
    searchable_by=["Ferroseed", "Basic", "Ferroseed"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=597,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.METAL: 2},
            damage=20,
        ),
    ],
)