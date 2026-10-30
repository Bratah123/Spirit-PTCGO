"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    unown_t_hidden_power,
    unown_throw,
)
from spirit.game.card_effects.ex import is_active_pokemon

card = PokemonCardDef(guid='ad04fa13-3f69-53c3-87a6-4be8c40def08', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownT.Name', display_name='Unown [T]', searchable_by=['Unown [T]', 'Basic', 'UnownT'], subtypes=['Basic'], collector_number=67, set_code='DP2', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='THROW', game_text="Once during your turn (before your attack), if Unown T is your Active Pokémon, you may discard a card from your hand. Then, flip a coin. If heads, put 2 damage counters on 1 of your opponent's Benched Pokémon. This power can't be used if Unown T is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=unown_throw(), activation=Activations.ONCE_PER_TURN, condition=is_active_pokemon), Attack(title='Hidden Power', game_text="Look at your opponent's hand and choose 1 card, then have your opponent shuffle that card into his or her deck. Then, show your opponent your hand and he or she chooses 1 card. Shuffle that card into your deck.", cost={PokemonTypes.COLORLESS: 1}, effect=unown_t_hidden_power())])
