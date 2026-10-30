"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_exeggutor_54_psychic_strategy,
    dp6_exeggutor_54_super_eggsplosion,
)

card = PokemonCardDef(guid='2328993a-c00a-5bcd-81d5-d6b85b456f33', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name', display_name='Exeggutor', searchable_by=['Exeggutor', 'Stage 1', 'Exeggutor'], subtypes=['Stage 1'], collector_number=54, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name', family_id=102, abilities=[Attack(title='Psychic Strategy', game_text="Each player counts the number of cards in his or her opponent's hand. Each player shuffles his or her hand into his or her deck. Then, each player draws a number of cards up to the number of cards his or her opponent had. (You draw your cards first.)", cost={}, effect=dp6_exeggutor_54_psychic_strategy()), Attack(title='Super Eggsplosion', game_text='Discard as many Energy cards as you like attached to your Pokémon. For each Energy card you discarded, flip a coin. This attack does 50 damage times the number of heads.', cost={PokemonTypes.PSYCHIC: 1}, damage=50, damage_operator='x', effect=dp6_exeggutor_54_super_eggsplosion())])
