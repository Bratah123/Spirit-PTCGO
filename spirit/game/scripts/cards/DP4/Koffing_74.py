"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_koffing_74_smogscreen,
)

card = PokemonCardDef(guid='1b4c3c63-47ad-5450-90f8-d7522a128e27', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name', display_name='Koffing', searchable_by=['Koffing', 'Basic', 'Koffing'], subtypes=['Basic'], collector_number=74, set_code='DP4', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=109, abilities=[Attack(title='Tackle', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Smogscreen', game_text="The Defending Pokémon is now Poisoned. If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=10, effect=dp4_koffing_74_smogscreen())])
