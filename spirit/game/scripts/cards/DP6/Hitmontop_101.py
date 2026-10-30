"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    dp6_hitmontop_101_gut_spin,
)

card = PokemonCardDef(guid='9c531979-4d20-597d-9069-5ebdd2ca456e', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name', display_name='Hitmontop', searchable_by=['Hitmontop', 'Basic', 'Hitmontop'], subtypes=['Basic'], collector_number=101, set_code='DP6', rarity=Rarities.Common, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=237, abilities=[Attack(title='Triple Kick', game_text='Flip 3 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='x', effect=flip_damage(coins=3, per_heads=20)), Attack(title='Gut Spin', game_text='If Tyrogue is anywhere under Hitmontop, you may switch Hitmontop with 1 of your Benched Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=dp6_hitmontop_101_gut_spin())])
