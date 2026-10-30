from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import assistance_cure, expand_protect, poke_power_condition

card = PokemonCardDef(
    guid="2cf9eda7-7502-5393-9fe4-e9dbad979e52",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Ability(
            title="Assistance",
            game_text="Once during your turn (before your attack), if Wigglytuff is on your Bench, you may choose 1 of your Active Pok\u00e9mon and remove 1 Special Condition from it.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=assistance_cure(),
        ),
        Attack(
            title="Expand",
            game_text="During your opponent's next turn, any damage done to Wigglytuff by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=expand_protect(10),
        ),
    ],
)