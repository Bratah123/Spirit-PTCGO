"""Rayquaza C LV.X (DPP #DP47)."""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dpp_rayquazaclvx_dp47_dragon_spirit_on_damaged,
    dpp_rayquazaclvx_dp47_final_blowup,
)

card = PokemonCardDef(
    guid='fa827502-e432-59ba-a416-efc7e08359c9',
    key='DPP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaCLVX.Name',
    display_name='Rayquaza C LV.X',
    searchable_by=['Rayquaza C LV.X', 'Level-Up', 'SP', 'RayquazaCLVX'],
    subtypes=['Level-Up', 'SP'],
    collector_number=47,
    set_code='DPP',
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaC.Name',
    family_id=384,
    abilities=[
        Ability(
            title='Dragon Spirit',
            game_text="If Rayquaza C is your Active Pokémon and is damaged but not Knocked Out by an opponent's attack, you may search your discard pile for an Energy card and attach it to Rayquaza C.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=dpp_rayquazaclvx_dp47_dragon_spirit_on_damaged,
        ),
        Attack(
            title='Final Blowup',
            game_text='Discard all Energy attached to Rayquaza C. Ignore this effect if you have no cards in your hand.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=dpp_rayquazaclvx_dp47_final_blowup(),
        ),
    ],
)
