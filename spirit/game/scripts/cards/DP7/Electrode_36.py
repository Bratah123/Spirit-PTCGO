"""Electrode (DP7 #36)."""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_salamence_18_direct_hit,
    dp7_electrode_36_low_current,
    dp7_electrode_36_radiance_on_damaged,
)

card = PokemonCardDef(
    guid='e0aa5208-ea40-5f36-98d9-429f4c2f2e9c',
    key='DP7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name',
    display_name='Electrode',
    searchable_by=['Electrode', 'Stage 1', 'Electrode'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='DP7',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    family_id=100,
    abilities=[
        Ability(
            title='Radiance',
            game_text="If Electrode is your Active Pokémon and is damaged by an opponent's attack (even if Electrode is Knocked Out), put 1 damage counter on each of your opponent's Pokémon.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=dp7_electrode_36_radiance_on_damaged,
        ),
        Attack(
            title='Low Current',
            game_text="If Electrode was damaged by an attack during your opponent's last turn, the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=dp7_electrode_36_low_current(),
        ),
        Attack(
            title='Swift',
            game_text="This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=dp3_salamence_18_direct_hit(),
        ),
    ],
)
