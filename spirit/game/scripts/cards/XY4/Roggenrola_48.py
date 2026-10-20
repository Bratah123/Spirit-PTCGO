from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b96b897-2d49-5a93-bb38-9f17847644a5",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    display_name="Roggenrola",
    searchable_by=["Roggenrola", "Basic", "Roggenrola"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=524,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)