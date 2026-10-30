"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_swampert_9_hammer_arm,
    dp4_swampert_9_wash_out,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='82cf378b-dccf-5170-911e-ba78298fa2da', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name', display_name='Swampert', searchable_by=['Swampert', 'Stage 2', 'Swampert'], subtypes=['Stage 2'], collector_number=9, set_code='DP4', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name', family_id=258, abilities=[Ability(title='Wash Out', game_text="As often as you like during your turn (before your attack), you may move a Water or Fighting Energy attached to 1 of your Benched Pokémon to your Active Pokémon. This power can't be used if Swampert is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_swampert_9_wash_out(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Hammer Arm', game_text="Discard the top card from your opponent's deck.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2}, damage=80, effect=dp4_swampert_9_hammer_arm())])
