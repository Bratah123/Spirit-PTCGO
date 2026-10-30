"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import dp3_weavile_40_chip_off
from spirit.game.card_effects.dp import (
    dp6_ninjask_67_cast_off_shell,
)

card = PokemonCardDef(guid='80f62e61-eaab-5f4c-897d-15bb9e64f5e6', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name', display_name='Ninjask', searchable_by=['Ninjask', 'Stage 1', 'Ninjask'], subtypes=['Stage 1'], collector_number=67, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name', family_id=290, abilities=[Ability(title='Cast-off Shell', game_text="Once during your turn, when you play Ninjask from your hand to evolve 1 of your Pokémon and if your Bench isn't full, you may put Shedinja onto your Bench as a Basic Pokémon from your hand or your discard pile.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_ninjask_67_cast_off_shell(), activation=Activations.ONCE_PER_TURN), Attack(title='Chip Off', game_text='If your opponent has 6 or more cards in his or her hand, discard a number of cards without looking until your opponent has 5 cards left in his or her hand.', cost={PokemonTypes.GRASS: 1}, damage=30, effect=dp3_weavile_40_chip_off())])
