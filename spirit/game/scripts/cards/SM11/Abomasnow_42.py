from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.sm11 import quick_freeze

card = PokemonCardDef(guid='95480d40-7a87-5e2d-a2fe-e0649b3f2fe2', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name', display_name='Abomasnow', searchable_by=['Abomasnow', 'Stage 1', 'Abomasnow'], subtypes=['Stage 1'], collector_number=42, set_code='SM11', rarity=Rarities.Rare, hp=140, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=4, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name', family_id=459, abilities=[Attack(title='Quick Freeze', game_text="If your opponent's Active Pokémon has any Water Energy attached to it, it is now Paralyzed.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=70, effect=quick_freeze), Attack(title='Wild Tackle', game_text='This Pokémon does 20 damage to itself.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2}, damage=140, effect=recoil_attack(20))])
