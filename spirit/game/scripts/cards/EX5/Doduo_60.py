from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ff16a67-7dd8-5bf0-94b3-4a55b3a17066",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    display_name="Doduo",
    searchable_by=["Doduo", "Basic", "Doduo"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=84,
    abilities=[
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)