from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba97c322-7b7e-5c48-b7ad-726a8322cfc5",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    display_name="Treecko",
    searchable_by=["Treecko", "Basic", "Treecko"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=252,
    abilities=[
        Attack(
            title="Smack",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)