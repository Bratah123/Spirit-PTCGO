from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import extra_energy_damage, form_variation, poke_power_condition

card = PokemonCardDef(
    guid="c7d72122-7644-5628-828f-8d16f6977c20",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Form Variation",
            game_text="Once during your turn (before your attack), you may search your discard pile for a Basic Pok\u00e9mon (excluding Pok\u00e9mon-ex and Ditto) and switch it with Ditto. (Any cards attached to Ditto, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Place Ditto in the discard pile.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=form_variation(),
        ),
        Attack(
            title="Energy Ball",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Ditto but not used to pay for this attack's Energy cost. You can't add more then 20 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=extra_energy_damage(10, base=10),
        ),
    ],
)