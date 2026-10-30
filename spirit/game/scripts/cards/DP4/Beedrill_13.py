"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_beedrill_13_band_attack,
    multi_flip_damage,
)

card = PokemonCardDef(guid='55f585ad-2473-5b25-8a77-5c0e294ff2e0', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name', display_name='Beedrill', searchable_by=['Beedrill', 'Stage 2', 'Beedrill'], subtypes=['Stage 2'], collector_number=13, set_code='DP4', rarity=Rarities.Rare, hp=110, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name', family_id=13, abilities=[Attack(title='Band Attack', game_text='Does 30 damage times the number of Beedrill you have in play.', cost={PokemonTypes.GRASS: 1}, damage=30, damage_operator='x', effect=dp4_beedrill_13_band_attack()), Attack(title='Twineedle', game_text='Flip 2 coins. This attack does 50 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 3}, damage=50, damage_operator='x', effect=multi_flip_damage(2, 50))])
