from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    magnetic_flow, magnetic_flow_condition, steel_wave,
)


card = PokemonCardDef(
    guid="3313f51d-db5f-501f-9439-42a02bab6b72",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Magnetic Flow",
            game_text="Once during your turn (before your attack), if Magneton is your Active Pok\u00e9mon, you may flip a coin. If heads, choose 2 of your opponent's Pok\u00e9mon that have Energy cards attached to them. Choose 1 of the Energy cards attached to each of those Pok\u00e9mon and switch them between the Pok\u00e9mon. This power can't be used if Magneton is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=magnetic_flow_condition,
            effect=magnetic_flow,
        ),
        Attack(
            title="Steel Wave",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon that are the same type (color) as the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=steel_wave,
        ),
    ],
)
