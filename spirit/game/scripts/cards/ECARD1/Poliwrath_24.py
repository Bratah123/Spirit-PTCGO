from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.ecard import plunge, plunge_condition


card = PokemonCardDef(
    guid="bf21ff64-de86-5dab-a02b-d2518e3e1be7",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Plunge",
            game_text="Once during your turn (before your attack), if Poliwrath is on your Bench, you may flip a coin. If heads, take all Energy cards attached to your Active Pok\u00e9mon, if any, and attach them to Poliwrath. Then switch Poliwrath with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=plunge_condition,
            effect=plunge,
        ),
        Attack(
            title="Water Punch",
            game_text="Flip a number of coins equal to the amount of Water Energy attached to Poliwrath. This attack does 40 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=flip_damage(
                coins_from=count_energy("self", energy_type=PokemonTypes.WATER),
                bonus_per_heads=10,
            ),
        ),
    ],
)
