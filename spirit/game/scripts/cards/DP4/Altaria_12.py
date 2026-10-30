"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_altaria_12_cotton_cloud,
)
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='6d510828-eb01-5a65-899d-ff36d7710a8d', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name', display_name='Altaria', searchable_by=['Altaria', 'Stage 1', 'Altaria'], subtypes=['Stage 1'], collector_number=12, set_code='DP4', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name', family_id=333, abilities=[Attack(title='Dragonbreath', game_text='Flip a coin. If tails, this attack does nothing. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 1}, damage=40, effect=flip_or_nothing()), Attack(title='Cotton Cloud', game_text="During your opponent's next turn, any damage done to Altaria by attacks from your opponent's Evolved Pokémon is reduced by 30 (after applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 3}, damage=60, effect=dp4_altaria_12_cotton_cloud())])
