"""Shaymin LV.X (DPP #DP39)."""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dpp_shayminlvx_dp39_revenge_seed_passive,
    dpp_shayminlvx_dp39_energy_flare,
)

card = PokemonCardDef(
    guid='01860cdb-dd90-5ce4-adc4-7b120b5f15c0',
    key='DPP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShayminLVX.Name',
    display_name='Shaymin LV.X',
    searchable_by=['Shaymin LV.X', 'Level-Up', 'ShayminLVX'],
    subtypes=['Level-Up'],
    collector_number=39,
    set_code='DPP',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name',
    family_id=492,
    abilities=[
        Ability(
            title='Revenge Seed',
            game_text="If any of your Grass Pokémon were Knocked Out by damage from an opponent's attack during his or her last turn, each of Shaymin's attacks does 60 more damage to the Active Pokémon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=dpp_shayminlvx_dp39_revenge_seed_passive(),
        ),
        Attack(
            title='Energy Flare',
            game_text='You may move any number of Energy cards attached to your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=dpp_shayminlvx_dp39_energy_flare(),
        ),
    ],
)
