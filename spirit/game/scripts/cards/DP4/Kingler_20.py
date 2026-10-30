"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='000c4e4d-c66a-5ebc-adf1-7cc7e106208c', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name', display_name='Kingler', searchable_by=['Kingler', 'Stage 1', 'Kingler'], subtypes=['Stage 1'], collector_number=20, set_code='DP4', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name', family_id=98, abilities=[Attack(title='Crabhammer', cost={PokemonTypes.COLORLESS: 2}, damage=30), Attack(title='Scissor Blow', game_text='If the Defending Pokémon would be be Knocked Out by this attack, Kingler does 30 damage to itself.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=80, effect=recoil_attack(30, damage=80))])
