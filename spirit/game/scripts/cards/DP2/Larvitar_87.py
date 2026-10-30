"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    mountain_bite,
)

card = PokemonCardDef(guid='6ce92f17-ebca-5c82-ae36-5be9d205b887', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name', display_name='Larvitar', searchable_by=['Larvitar', 'Basic', 'Larvitar'], subtypes=['Basic'], collector_number=87, set_code='DP2', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=246, abilities=[Attack(title='Mountain Bite', game_text='You may discard the top card of your deck. If you do, this attack does 10 damage plus 10 more damage and Larvitar is now Asleep.', cost={PokemonTypes.FIGHTING: 1}, damage=10, damage_operator='+', effect=mountain_bite(10, 1)), Attack(title='Hammer In', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
