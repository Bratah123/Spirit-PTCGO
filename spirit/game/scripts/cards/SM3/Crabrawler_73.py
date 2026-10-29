from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="491215f6-f393-5108-a348-b6b18b903dd9",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    display_name="Crabrawler",
    searchable_by=["Crabrawler", "Basic", "Crabrawler"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=739,
    abilities=[
        Attack(
            title="Light Punch",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
        ),
    ],
)
