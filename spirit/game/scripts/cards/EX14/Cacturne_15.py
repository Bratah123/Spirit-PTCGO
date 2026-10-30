from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import spike_storm_counters, triple_breach


card = PokemonCardDef(
    guid="07ac6e60-459f-58dc-b96a-b2336963f0ac",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne δ",
    searchable_by=["Cacturne \u03b4", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="EX14",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Ability(
            title="Spike Storm",
            game_text="Once during your turn (before your attack), if Cacturne is your Active Pok\u00e9mon, you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon that already has any damage counters on it. This power can't be used if Cacturne is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
                        effect=spike_storm_counters(1),
        ),
        Attack(
            title="Triple Needle",
            game_text="Choose 3 of your opponent's Pok\u00e9mon. This attack does 10 damage to each of those Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=triple_breach(),
        ),
        Attack(
            title="Light Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)