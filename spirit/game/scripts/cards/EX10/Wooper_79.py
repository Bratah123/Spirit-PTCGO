from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3938e153-8054-510e-bb79-412a19268fb4",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name="Wooper",
    searchable_by=["Wooper", "Basic", "Wooper"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=194,
    abilities=[
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)