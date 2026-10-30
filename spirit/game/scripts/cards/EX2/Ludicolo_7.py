from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import extra_energy_damage, rain_dish


card = PokemonCardDef(
    guid="9fc2b763-f077-5be7-a973-8960604c7655",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Rain Dish",
            game_text="At any time between turns, remove 1 damage counter from Ludicolo.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=rain_dish(),
        ),
        Attack(
            title="Hydro Punch",
            game_text="Does 50 damage plus 10 more damage for each Water Energy attached to Ludicolo but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=extra_energy_damage(
                10, base=50, extra_cap=2, energy_type=PokemonTypes.WATER,
            ),
        ),
    ],
)
