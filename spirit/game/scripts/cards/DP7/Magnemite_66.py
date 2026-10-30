"""STUB: effect not implemented — do not guess mechanics.
Magnemite (DP7 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_magnemite_66_magnetic_bomb,
)

card = PokemonCardDef(guid='6e41a255-76b5-579f-8511-5bd8b3b5d7fa', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name', display_name='Magnemite', searchable_by=['Magnemite', 'Basic', 'Magnemite'], subtypes=['Basic'], collector_number=66, set_code='DP7', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=81, abilities=[Attack(title='Magnetic Bomb', game_text='Flip a coin. If heads, this attack does 30 damage plus 10 more damage. If tails, Magnemite does 10 damage to itself.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=dp7_magnemite_66_magnetic_bomb())])
