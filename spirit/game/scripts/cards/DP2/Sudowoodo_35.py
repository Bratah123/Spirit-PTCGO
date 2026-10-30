"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.passives_common import flip_protection
from spirit.game.card_effects.support_common import gust_attack

from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(guid='5ec54100-bfbf-5d5f-b9f3-52e6ba24907f', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name', display_name='Sudowoodo', searchable_by=['Sudowoodo', 'Basic', 'Sudowoodo'], subtypes=['Basic'], collector_number=35, set_code='DP2', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=185, abilities=[Attack(title='Sidestep', game_text="If Bonsly is anywhere under Sudowoodo, flip a coin. If heads, prevent all effects of an attack, including damage, done to Sudowoodo during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=flip_protection(prevent=True, effects_too=True, title='Sidestep')), Attack(title='Persuade', game_text="Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon. The new Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.FIGHTING: 2}, damage=30, effect=gust_attack(opponent_chooses=True))])
