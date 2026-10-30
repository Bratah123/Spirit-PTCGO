"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_uxie_43_psychic_restore,
    dp6_uxie_43_set_up,
)

card = PokemonCardDef(guid='60517751-4494-5c78-9ecb-ecd98ce303ce', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name', display_name='Uxie', searchable_by=['Uxie', 'Basic', 'Uxie'], subtypes=['Basic'], collector_number=43, set_code='DP6', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=480, abilities=[Ability(title='Set Up', game_text='Once during your turn, when you put Uxie from your hand onto your Bench, you may draw cards until you have 7 cards in your hand.', ability_type=AbilityTypes.POKE_POWER, effect=dp6_uxie_43_set_up(), activation=Activations.ONCE_PER_TURN), Attack(title='Psychic Restore', game_text='You may put Uxie and all cards attached to it on the bottom of your deck in any order.', cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=dp6_uxie_43_psychic_restore())])
