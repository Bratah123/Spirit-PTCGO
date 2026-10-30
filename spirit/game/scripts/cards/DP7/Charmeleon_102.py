"""STUB: effect not implemented — do not guess mechanics.
Charmeleon (DP7 #102): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(guid='0ad59c77-ecbb-5a08-9225-ab67ddeef4a1', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name', display_name='Charmeleon', searchable_by=['Charmeleon', 'Stage 1', 'Charmeleon'], subtypes=['Stage 1'], collector_number=102, set_code='DP7', rarity=Rarities.RareSecret, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name', family_id=4, abilities=[Attack(title='Slash', cost={PokemonTypes.COLORLESS: 3}, damage=30), Attack(title='Flamethrower', game_text='Discard a Fire Energy attached to Charmeleon.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=self_energy_discard_attack(count=1, then_damage=50))])
