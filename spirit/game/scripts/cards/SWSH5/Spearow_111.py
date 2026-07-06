from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86fb4ab9-1025-5958-ab7e-ff98d1ca4de4",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    display_name="Spearow",
    searchable_by=["Spearow", "Basic", "Spearow"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=21,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)