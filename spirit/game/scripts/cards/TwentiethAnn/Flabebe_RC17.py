from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="980f69ab-5111-5295-ab3f-167d73e5f210",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    display_name="Flab\u00e9b\u00e9",
    searchable_by=["Flabébé", "Basic", "Flabebe"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="TwentiethAnn",
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