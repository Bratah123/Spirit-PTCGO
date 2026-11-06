from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d0f3ecd7-e2b8-516b-a699-052da51ec2b9",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic", "Diglett"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BASE1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=50,
    abilities=[
        Attack(
            title="Dig",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)