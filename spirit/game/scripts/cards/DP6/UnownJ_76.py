"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_unownj_76_hidden_power,
    dp6_unownj_76_junk,
)

card = PokemonCardDef(guid='a22141ac-1b4e-53d8-971a-3107ac0e050a', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownJ.Name', display_name='Unown [J]', searchable_by=['Unown [J]', 'Basic', 'UnownJ'], subtypes=['Basic'], collector_number=76, set_code='DP6', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='JUNK', game_text='Once during your turn, when you put Unown J from your hand onto your Bench, you may flip a coin. If heads, search your discard pile for a Trainer card, show it to your opponent, and put it into your hand.', ability_type=AbilityTypes.POKE_POWER, effect=dp6_unownj_76_junk(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Remove the Special Condition Asleep from the Defending Pokémon.', cost={PokemonTypes.PSYCHIC: 1}, damage=10, effect=dp6_unownj_76_hidden_power())])
