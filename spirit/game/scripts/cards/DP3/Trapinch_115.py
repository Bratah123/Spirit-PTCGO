"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import magma_ring_no_retreat
from spirit.game.card_effects.support_common import gust_attack

card = PokemonCardDef(guid='12ca16ec-9678-5d3d-a43d-f159eb7e3045', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name', display_name='Trapinch', searchable_by=['Trapinch', 'Basic', 'Trapinch'], subtypes=['Basic'], collector_number=115, set_code='DP3', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=328, abilities=[Attack(title='Inviting Trap', game_text="Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon.", cost={PokemonTypes.COLORLESS: 1}, effect=gust_attack()), Attack(title='Sand Tomb', game_text="The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.FIGHTING: 1}, damage=10, effect=magma_ring_no_retreat())])
