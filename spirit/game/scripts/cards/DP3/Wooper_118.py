"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp3_wooper_118_splatter,
)

card = PokemonCardDef(guid='a2cd42f8-26af-52f2-800c-43ce58c4c750', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name', display_name='Wooper', searchable_by=['Wooper', 'Basic', 'Wooper'], subtypes=['Basic'], collector_number=118, set_code='DP3', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=194, abilities=[Attack(title='Yawn', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Splatter', game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon. This attack's damage isn't affected by Weakness or Resistance.", cost={PokemonTypes.WATER: 1}, effect=dp3_wooper_118_splatter())])
