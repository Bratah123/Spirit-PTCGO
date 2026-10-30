"""STUB: effect not implemented — do not guess mechanics.
Ponyta (DP7 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(guid='23270e4b-1c34-5e50-b9ec-4075167c73b6', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name', display_name='Ponyta', searchable_by=['Ponyta', 'Basic', 'Ponyta'], subtypes=['Basic'], collector_number=71, set_code='DP7', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=77, abilities=[Attack(title='Smash Kick', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Agility', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Ponyta during your opponent's next turn.", cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=flip_protection(prevent=True, effects_too=True, title='Agility'))])
