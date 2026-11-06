from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import evolution_helper, evolution_helper_condition


card = PokemonCardDef(
    guid="ca57adb7-4086-5d79-a186-e86ff913d51a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=22,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Evolution Helper",
            game_text="Once during your turn (before your attack), if Nidoqueen is on your Bench, you may search your deck for a card that evolves from your Active Pok\u00e9mon and attach it to your Active Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=evolution_helper_condition,
            effect=evolution_helper,
        ),
        Attack(
            title="Double Claw",
            game_text="Flip 2 coins. This attack does 30 damage plus 20 more damage for each heads",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)
