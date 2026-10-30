"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_unownr_77_hidden_power,
    dp6_unownr_77_retire,
)

card = PokemonCardDef(guid='cee5d918-476c-5532-9d1b-6ce1d06de7ac', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownR.Name', display_name='Unown [R]', searchable_by=['Unown [R]', 'Basic', 'UnownR'], subtypes=['Basic'], collector_number=77, set_code='DP6', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='RETIRE', game_text="Once during your turn, if Unown R is on your Bench, you may discard Unown R and all cards attached to it. (This doesn't count as a Knocked Out Pokémon.) Then, draw a card.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_unownr_77_retire(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Move any number of basic Energy cards attached to your Pokémon to your other Pokémon in any way you like.', cost={}, effect=dp6_unownr_77_hidden_power())])
