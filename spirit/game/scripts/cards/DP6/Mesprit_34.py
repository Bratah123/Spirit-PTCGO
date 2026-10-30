"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_mesprit_34_extrasensory,
    dp6_mesprit_34_psychic_bind,
)

card = PokemonCardDef(guid='92488a8c-58a6-5fd1-8312-7417b2175424', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name', display_name='Mesprit', searchable_by=['Mesprit', 'Basic', 'Mesprit'], subtypes=['Basic'], collector_number=34, set_code='DP6', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=481, abilities=[Ability(title='Psychic Bind', game_text="Once during your turn, when you put Mesprit from your hand onto your Bench, you may use this power. Your opponent can't use any Poké-Powers on his or her Pokémon during your opponent's next turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_mesprit_34_psychic_bind(), activation=Activations.ONCE_PER_TURN), Attack(title='Extrasensory', game_text='If you have the same number of cards in your hand as your opponent, this attack does 20 damage plus 50 more damage.', cost={PokemonTypes.PSYCHIC: 2}, damage=20, damage_operator='+', effect=dp6_mesprit_34_extrasensory())])
