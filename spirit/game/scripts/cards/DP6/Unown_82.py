"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_unown_82_effect,
    dp6_unown_82_hidden_power,
)

card = PokemonCardDef(guid='21b76a27-7bd2-5a06-8200-a8572810e378', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name', display_name='Unown [?]', searchable_by=['Unown [?]', 'Basic', 'Unown'], subtypes=['Basic'], collector_number=82, set_code='DP6', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='?', game_text='Once during your turn (before your attack), if Unown ? is on your Bench, you may choose a Pokémon in your hand and put it face down. Your opponent guesses a type of that Pokémon. Reveal that card. If your opponent guessed wrong, draw a card. Then, put that card back into your hand.', ability_type=AbilityTypes.POKE_POWER, effect=dp6_unown_82_effect(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Discard up to 2 cards from your hand. For each card you discarded, draw a card.', cost={}, effect=dp6_unown_82_hidden_power())])
