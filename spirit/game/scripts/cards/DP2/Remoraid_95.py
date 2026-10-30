"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='493ba846-2c74-5dc0-af2a-03a2ec10c37b', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name', display_name='Remoraid', searchable_by=['Remoraid', 'Basic', 'Remoraid'], subtypes=['Basic'], collector_number=95, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=223, abilities=[Attack(title='Sharpshooting', game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1}, effect=snipe_attack(20, pool='any')), Attack(title='Numbing Water', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.WATER: 2}, damage=20, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
