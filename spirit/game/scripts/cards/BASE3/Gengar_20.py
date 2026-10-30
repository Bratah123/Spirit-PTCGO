from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import curse, curse_condition


card = PokemonCardDef(
    guid="c26a8c9a-b8ec-5ea1-875e-d0860daa1cb2",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="BASE3",
    rarity=Rarities.Rare,
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
            game_text="Once during your turn (before your attack), you may move 1 damage counter from 1 of your opponent's Pok\u00e9mon to another (even if it would Knock Out the other Pok\u00e9mon). This power can't be used if Gengar is Asleep, Confused, or Paralyzed.",
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
