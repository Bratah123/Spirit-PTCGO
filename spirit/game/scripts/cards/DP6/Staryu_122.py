"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(guid='cb4fd053-e92b-59bd-8f3c-1c7883e7b629', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name', display_name='Staryu', searchable_by=['Staryu', 'Basic', 'Staryu'], subtypes=['Basic'], collector_number=122, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=120, abilities=[Attack(title='Recover', game_text='Discard an Energy attached to Staryu and remove 3 damage counters from Staryu.', cost={PokemonTypes.COLORLESS: 1}, effect=self_energy_discard_attack(count=1, then_damage=0)), Attack(title='Spinning Attack', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=20)])
