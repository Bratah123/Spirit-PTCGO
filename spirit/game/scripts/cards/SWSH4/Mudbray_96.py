from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="406f9c99-2b36-530a-8a77-e59df6d61bb4",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    display_name="Mudbray",
    searchable_by=["Mudbray", "Basic", "Mudbray"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=749,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)