from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="15494229-d794-533c-bafe-c6bd8420fb3a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesSpearow.Name",
    display_name="Lt. Surge's Spearow",
    searchable_by=["Lt. Surge's Spearow", "Basic", "LtSurgesSpearow"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=21,
    abilities=[
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)