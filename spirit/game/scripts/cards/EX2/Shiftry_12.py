from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.ex import flip_return_defender_energy, poke_power_condition


card = PokemonCardDef(
    guid="a5bfa8d8-1e08-5ddb-a4f3-ff0c726d44c4",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Fan Away",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, return 1 Energy card attached to the Defending Pok\u00e9mon to your opponent's hand. This power can't be used if Shiftry is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=flip_return_defender_energy(),
        ),
        Attack(
            title="Light Touch Throw",
            game_text="Does 80 damage minus 10 damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="-",
            effect=damage_per(count_energy("defender"), per=-10, base=80),
        ),
    ],
)
