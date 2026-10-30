"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.support_common import heal_targets

from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack

card = PokemonCardDef(guid='19b17af1-c167-55dd-8cbe-638aeb83debf', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name', display_name='Tropius', searchable_by=['Tropius', 'Basic', 'Tropius'], subtypes=['Basic'], collector_number=64, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=357, abilities=[Attack(title='Bonus Leaf', game_text='Remove 3 damage counters from each of your Benched Pokémon that has any Grass Energy attached to it.', cost={PokemonTypes.GRASS: 1}, effect=heal_targets(30, scope='each_own')), Attack(title='Whirlwind', game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=gust_attack(opponent_chooses=True))])
