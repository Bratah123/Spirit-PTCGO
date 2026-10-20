from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="55bb319e-8dd3-5b74-8665-6783872b2140",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="Flab\u00e9b\u00e9",
    searchable_by=["Flabébé", "Basic", "Flabb"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)