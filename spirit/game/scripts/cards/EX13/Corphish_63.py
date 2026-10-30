"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    flail_per_counter,
)

card = PokemonCardDef(guid='9c0bbc41-590a-5204-8464-d9301c6d9489', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name', display_name='Corphish', searchable_by=['Corphish', 'Basic', 'Corphish'], subtypes=['Basic'], collector_number=63, set_code='EX13', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=341, abilities=[Attack(title='Flail', game_text='Does 10 damage times the number of damage counters on Corphish.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flail_per_counter(10)), Attack(title='Crabhammer', cost={PokemonTypes.WATER: 1}, damage=10)])
