from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c24d22db-651c-5ac2-a4fd-ca6db118c9fc",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    display_name="Mudbray",
    searchable_by=["Mudbray", "Basic", "Mudbray"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=749,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)