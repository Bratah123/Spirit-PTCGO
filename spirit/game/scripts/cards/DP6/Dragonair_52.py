"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(guid='129cf307-3e04-5edc-b8f7-be2c10fd32fb', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name', display_name='Dragonair', searchable_by=['Dragonair', 'Stage 1', 'Dragonair'], subtypes=['Stage 1'], collector_number=52, set_code='DP6', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.COLORLESS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name', family_id=147, abilities=[Attack(title='Wrap', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Rising Lunge', game_text='Flip a coin. If heads, this attack does 30 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 3}, damage=30, damage_operator='+', effect=flip_bonus(20))])
