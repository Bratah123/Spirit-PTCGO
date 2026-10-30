"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_tauros_74_herd_charge,
    dp6_tauros_74_thrash,
)

card = PokemonCardDef(guid='991d1389-1649-5a8b-ad91-f25d3b3da1ea', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name', display_name='Tauros', searchable_by=['Tauros', 'Basic', 'Tauros'], subtypes=['Basic'], collector_number=74, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=128, abilities=[Attack(title='Herd Charge', game_text='Flip a coin for each Tauros you have in play. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=dp6_tauros_74_herd_charge()), Attack(title='Thrash', game_text='Flip a coin. If heads, this attack does 40 damage plus 20 more damage. If tails, Tauros does 10 damage to itself.', cost={PokemonTypes.COLORLESS: 3}, damage=40, damage_operator='+', effect=dp6_tauros_74_thrash())])
