from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


card = PokemonCardDef(
    guid="036df38b-cfb8-507f-8646-1dbeccbe9de3",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Sudowoodo.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 10),
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
