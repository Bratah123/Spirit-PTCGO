from spirit.game.card_effects.dp import heal_then_damage_defender
"""STUB: effect not implemented — do not guess mechanics.
Teddiursa (DP2 #105): one or more attacks/abilities use effect=heal_then_damage_defender(10, 30) until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import rest_attack

card = PokemonCardDef(guid='b035d9a5-dace-5fb1-aa91-8b2708a20811', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name', display_name='Teddiursa', searchable_by=['Teddiursa', 'Basic', 'Teddiursa'], subtypes=['Basic'], collector_number=105, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=216, abilities=[Attack(title='Rest', game_text='Remove all Special Conditions and 2 damage counters from Teddiursa. Teddiursa is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=rest_attack(counters=2)), Attack(title='Sweet Palm', game_text='Before doing damage, remove 1 damage counter from the Defending Pokémon.', cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=heal_then_damage_defender(10, 30))])
