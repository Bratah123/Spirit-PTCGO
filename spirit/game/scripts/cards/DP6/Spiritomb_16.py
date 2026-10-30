"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_spiritomb_16_curse_breath,
    dp6_spiritomb_16_transfer_pain,
)

card = PokemonCardDef(guid='148f8b56-db87-5d6d-b1dd-1c729cf0b8b7', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name', display_name='Spiritomb', searchable_by=['Spiritomb', 'Basic', 'Spiritomb'], subtypes=['Basic'], collector_number=16, set_code='DP6', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=442, abilities=[Ability(title='Curse Breath', game_text="Once during your turn, when you put Spiritomb from your hand onto your Bench, you may put 1 damage counter on all Pokémon that already have any damage counters on them (both yours and your opponent's). You can't use more than 1 Curse Breath Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_spiritomb_16_curse_breath(), activation=Activations.ONCE_PER_TURN), Attack(title='Transfer Pain', game_text="Move 1 damage counter from 1 of your Pokémon to 1 of your opponent's Pokémon.", cost={PokemonTypes.PSYCHIC: 1}, effect=dp6_spiritomb_16_transfer_pain())])
