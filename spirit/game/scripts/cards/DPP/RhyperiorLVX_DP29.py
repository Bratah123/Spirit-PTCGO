"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_rhyperiorlvx_145_hard_crush,
    dp6_rhyperiorlvx_145_upthrow,
)

card = PokemonCardDef(guid='9ed5586f-91b4-54c9-8090-85479d367a85', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.RhyperiorLVX.Name', display_name='Rhyperior LV.X', searchable_by=['Rhyperior LV.X', 'Level-Up', 'RhyperiorLVX'], subtypes=['Level-Up'], collector_number=29, set_code='DP6', rarity=Rarities.RareHolo, hp=170, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.LEVELUP, retreat_cost=4, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name', family_id=464, abilities=[Attack(title='Hard Crush', game_text='Discard the top 5 cards from your deck. This attack does 50 damage for each Energy card you discarded.', cost={}, damage=50, damage_operator='x', effect=dp6_rhyperiorlvx_145_hard_crush()), Attack(title='Upthrow', game_text='Search your discard pile for all Fighting Energy cards, show them to your opponent, and shuffle them into your deck.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp6_rhyperiorlvx_145_upthrow())])
