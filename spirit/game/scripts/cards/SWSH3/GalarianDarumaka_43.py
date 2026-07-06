from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76781eec-f6c2-5151-ba18-47ca7947928e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarumaka.Name",
    display_name="Galarian Darumaka",
    searchable_by=["Galarian Darumaka", "Basic", "GalarianDarumaka"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=554,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)