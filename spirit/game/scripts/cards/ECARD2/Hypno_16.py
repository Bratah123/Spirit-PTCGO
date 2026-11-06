from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    sleep_pendulum, sleep_pendulum_condition, spiral_aura,
)


card = PokemonCardDef(
    guid="1d9881f2-d3cb-5fd4-bd7d-18c14f7b324f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Sleep Pendulum",
            game_text="Once during your turn (before your attack), if Hypno is your Active Pok\u00e9mon, you may make the Defending Pok\u00e9mon Asleep. This power can't be used if Hypno is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=sleep_pendulum_condition,
            effect=sleep_pendulum,
        ),
        Attack(
            title="Spiral Aura",
            game_text="If the Defending Pok\u00e9mon isn't Knocked Out by the damage from this attack, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch the Defending Pok\u00e9mon with it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=spiral_aura,
        ),
    ],
)
