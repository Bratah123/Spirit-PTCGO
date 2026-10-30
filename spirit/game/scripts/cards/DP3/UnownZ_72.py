"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_unownz_72_hidden_power,
    dp3_unownz_72_zero,
)

card = PokemonCardDef(guid='2dd7a530-9cd2-57e3-9856-418a394061e9', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownZ.Name', display_name='Unown [Z]', searchable_by=['Unown [Z]', 'Basic', 'UnownZ'], subtypes=['Basic'], collector_number=72, set_code='DP3', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='ZERO', game_text='Once during your turn (before your attack), if Unown Z is on your Bench and you have no cards in your deck, you may discard all cards attached to Unown Z and put Unown Z on top of your deck.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_unownz_72_zero(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Remove as many damage counters as you like from each Unown you have in play. Put that many damage counters on the Defending Pokémon.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, effect=dp3_unownz_72_hidden_power())])
