from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import curse, curse_condition


card = PokemonCardDef(
    guid="649d88eb-f9ac-5f33-bc10-197ad5c875d5",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Curse",
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 of your opponent's Pok\u00e9mon to another (even if it would Knock Out the other Pok\u00e9mon). This power can't be used if Gengar is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=curse_condition,
            effect=curse,
        ),
        Attack(
            title="Dark Mind",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            effect=snipe_attack(10, also_base=True),
        ),
    ],
)
