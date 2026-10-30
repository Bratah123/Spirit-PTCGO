"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_natu_96_future_sight,
)
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='32459d56-df08-59c0-8340-fd2a0f6c571b', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name', display_name='Natu', searchable_by=['Natu', 'Basic', 'Natu'], subtypes=['Basic'], collector_number=96, set_code='DP3', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=177, abilities=[Attack(title='Bothering Wave', game_text='Flip a coin. If tails, this attack does nothing. If heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=flip_or_nothing()), Attack(title='Future Sight', game_text="Look at the top 5 cards of either player's deck and put them back on top of that player's deck in any order.", cost={PokemonTypes.PSYCHIC: 1}, effect=dp3_natu_96_future_sight())])
