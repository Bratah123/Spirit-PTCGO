"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_bellsprout_85_careless_tackle,
    dp6_bellsprout_85_vine_bind,
)

card = PokemonCardDef(guid='5e2e25b9-bbd5-54e5-b275-f6a5b2192c2d', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name', display_name='Bellsprout', searchable_by=['Bellsprout', 'Basic', 'Bellsprout'], subtypes=['Basic'], collector_number=85, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=69, abilities=[Attack(title='Vine Bind', game_text="Flip a coin. If heads, the Defending Pokémon can't use any Poké-Powers during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=dp6_bellsprout_85_vine_bind()), Attack(title='Careless Tackle', game_text='Bellsprout does 10 damage to itself.', cost={PokemonTypes.GRASS: 1}, damage=20, effect=dp6_bellsprout_85_careless_tackle())])
