"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_ledyba_104_double_edge,
)

card = PokemonCardDef(guid='5459d9a2-c61f-5f69-9647-9c2b0a59ba3f', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name', display_name='Ledyba', searchable_by=['Ledyba', 'Basic', 'Ledyba'], subtypes=['Basic'], collector_number=104, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=165, abilities=[Attack(title='Supersonic', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.CONFUSED, flip=True)), Attack(title='Double-edge', game_text='Ledyba does 10 damage to itself.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=dp6_ledyba_104_double_edge())])
