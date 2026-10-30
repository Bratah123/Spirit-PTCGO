"""STUB: effect not implemented — do not guess mechanics.
Voltorb (DP7 #80): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    dp7_voltorb_80_screech,
)

card = PokemonCardDef(guid='e6c127f6-1be0-5df2-8a33-95d4d6e7845a', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name', display_name='Voltorb', searchable_by=['Voltorb', 'Basic', 'Voltorb'], subtypes=['Basic'], collector_number=80, set_code='DP7', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=100, abilities=[Attack(title='Screech', game_text='If an attack does damage to the Defending Pokémon (after applying Weakness and Resistance), that attack does 20 more damage to that Pokémon until the end of your next turn.', cost={}, effect=dp7_voltorb_80_screech()), Attack(title='Double Spin', game_text='Flip 2 coins. This attack does 10 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flip_damage(coins=2, per_heads=10))])
