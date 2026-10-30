"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import call_for_family_basic_n
from spirit.game.card_effects.ex import (
    flail_per_counter,
)

card = PokemonCardDef(guid='c6aa246a-606a-5e29-86f2-f6f2253d7af2', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name', display_name='Wobbuffet', searchable_by=['Wobbuffet', 'Basic', 'Wobbuffet'], subtypes=['Basic'], collector_number=56, set_code='EX13', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=202, abilities=[Attack(title='Call for Friends', game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=call_for_family_basic_n(2)), Attack(title='Retaliate', game_text='Does 10 damage times the number of damage counters on Wobbuffet.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flail_per_counter(10))])
