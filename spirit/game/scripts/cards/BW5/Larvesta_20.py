from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="99696421-2ace-504a-a449-0aa6820f6e98",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    display_name="Larvesta",
    searchable_by=["Larvesta", "Basic", "Larvesta"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=636,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)