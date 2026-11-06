from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import beating_wings, beating_wings_condition


card = PokemonCardDef(
    guid="b7e2f858-d4d5-53b8-8e7e-b1d2ff149d9a",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Ability(
            title="Beating Wings",
            game_text="Once during your turn (before your attack), if Pidgeot is your Active Pok\u00e9mon, you may shuffle 1 of your Benched Pok\u00e9mon and all cards attached to it into your deck. This power can't be used if Pidgeot is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=beating_wings_condition,
            effect=beating_wings,
        ),
        Attack(
            title="Sharp Beak",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
