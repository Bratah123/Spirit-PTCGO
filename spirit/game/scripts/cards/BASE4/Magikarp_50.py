from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


card = PokemonCardDef(
    guid="cc2bbb26-45d9-5435-868b-be2b7efafa8b",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Magikarp.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 10),
        ),
    ],
)
