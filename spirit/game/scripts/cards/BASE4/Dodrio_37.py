from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.card_effects.ecard import RetreatAidPassive


card = PokemonCardDef(
    guid="e26dd66e-ecbe-57ae-8998-365395a09c40",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=85,
    abilities=[
        Ability(
            title="Retreat Aid",
            game_text="As long as Dodrio is Benched, pay Colorless less to retreat your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=RetreatAidPassive(),
        ),
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Dodrio.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=10),
        ),
    ],
)
