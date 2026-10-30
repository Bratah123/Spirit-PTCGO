"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    reckless_charge_recoil,
)

card = PokemonCardDef(guid='787e9a55-2e12-537d-8fe8-706d06039978', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name', display_name='Carvanha δ', searchable_by=['Carvanha δ', 'Basic', 'Carvanha'], subtypes=['Basic'], collector_number=61, set_code='EX13', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=318, abilities=[Attack(title='Bite', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Reckless Charge', game_text='Flip a coin. If tails, Carvanha does 10 damage to itself.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=reckless_charge_recoil(10))])
