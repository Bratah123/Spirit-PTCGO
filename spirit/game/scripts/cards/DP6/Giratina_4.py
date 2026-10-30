"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_giratina_4_brutal_edge,
)
from spirit.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(guid='9716b7c8-ce3a-50d8-8cab-fa43b320a3c5', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name', display_name='Giratina', searchable_by=['Giratina', 'Basic', 'Giratina'], subtypes=['Basic'], collector_number=4, set_code='DP6', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=487, abilities=[Attack(title='Shadow Force', game_text="Choose 1 of your opponent's Benched Pokémon. This attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Flip a coin. If heads, prevent all effects of an attack, including damage, done to Giratina during your opponent's next turn.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, effect=flip_protection(prevent=True, effects_too=True, title='Shadow Force')), Attack(title='Brutal Edge', game_text='Does 50 damage plus 10 more damage for each damage counter on the Defending Pokémon.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=dp6_giratina_4_brutal_edge())])
