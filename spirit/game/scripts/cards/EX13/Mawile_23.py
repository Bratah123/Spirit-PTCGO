"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import shuffle_random_from_opponent_hand
from spirit.game.card_effects.ex import (
    feint_attack,
)

card = PokemonCardDef(guid='21b5953e-0618-5163-ae22-bda76455065a', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name', display_name='Mawile', searchable_by=['Mawile', 'Basic', 'Mawile'], subtypes=['Basic'], collector_number=23, set_code='EX13', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.GRASS, family_id=303, abilities=[Attack(title='Feint Attack', game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.COLORLESS: 1}, effect=feint_attack(20)), Attack(title='Surprise', game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.", cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=shuffle_random_from_opponent_hand())])
