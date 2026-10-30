"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_mew_15_psychic_balance,
    dp3_mew_15_re_creation,
)

card = PokemonCardDef(guid='ccc22302-54f6-5005-bb49-fbbeb407f251', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name', display_name='Mew', searchable_by=['Mew', 'Basic', 'Mew'], subtypes=['Basic'], collector_number=15, set_code='DP3', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=151, abilities=[Attack(title='Psychic Balance', game_text='If you have less cards in your hand than your opponent, draw cards until you have the same number of cards as your opponent. (If you have more or the same number of cards in your hand as your opponent, this attack does nothing.)', cost={}, effect=dp3_mew_15_psychic_balance()), Attack(title='Re-creation', game_text="Choose an attack on 1 of your opponent's Pokémon in his or her discard pile. Re-creation copies that attack except for its Energy cost. (You must still do anything else required for that attack.) Mew performs that attack.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, effect=dp3_mew_15_re_creation())])
