from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="baee4375-a8f9-50b8-8791-d687fe68d58a",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    display_name="Staryu",
    searchable_by=["Staryu", "Basic", "Staryu"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)