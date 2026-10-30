"""STUB: effect not implemented — do not guess mechanics.
Regirock ★ (EX12 #91): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    dig_drain_heal,
    final_blast_boost,
)

card = PokemonCardDef(guid='a03c815e-d696-50fa-8b32-42b78e740edf', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name', display_name='Regirock ★', searchable_by=['Regirock ★', 'Basic', 'Star', 'Regirock'], subtypes=['Basic', 'Star'], collector_number=91, set_code='EX12', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.WATER, family_id=377, abilities=[Attack(title='Dig Drain', game_text='Remove 1 damage counter from Regirock Star.', cost={PokemonTypes.FIGHTING: 1}, damage=10, effect=dig_drain_heal(1)), Attack(title='Final Blast', game_text="If your opponent has only 1 Prize card left and Regirock Star is the only Pokémon you have in play, this attack's base damage is 100 instead of 30.", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=30, effect=final_blast_boost(50, 100))])
