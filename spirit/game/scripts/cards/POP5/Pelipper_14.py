from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import mist_vs_stage2_passive, snipe_own_bench


card = PokemonCardDef(
    guid="348421e9-a8dc-53c3-be55-caf30537714b",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper δ",
    searchable_by=["Pelipper \u03b4", "Stage 1", "Pelipper"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="POP5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=279,
    abilities=[
        Ability(
            title="Mist",
            game_text="Any damage done to Pelipper by attacks from Stage 2 Evolved Pokémon (both yours and your opponent's) is reduced by 30 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=mist_vs_stage2_passive(30),
            effect=None,
        ),
        Attack(
            title="Lightning Wing",
            game_text="Does 10 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=snipe_own_bench(10),
        ),
    ],
)
