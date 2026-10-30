"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_unownh_29_heal,
    dp4_unownh_29_hidden_power,
)

card = PokemonCardDef(guid='a6a3e6da-d562-5482-99ee-8b44fe72edb2', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownH.Name', display_name='Unown [H]', searchable_by=['Unown [H]', 'Basic', 'UnownH'], subtypes=['Basic'], collector_number=29, set_code='DP4', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='HEAL', game_text='Once during your turn (before your attack), if you have Unown H, Unown E, Unown A, and Unown L on your Bench, you may remove all Special Conditions from 1 of your Active Pokémon.', ability_type=AbilityTypes.POKE_POWER, effect=dp4_unownh_29_heal(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text="Discard a card from your hand. (If you can't discard a card from your hand, this attack does nothing.)", cost={PokemonTypes.PSYCHIC: 1}, damage=30, effect=dp4_unownh_29_hidden_power())])
