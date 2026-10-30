"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(guid='1ec56388-1488-5524-8505-9f8eed473ada', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name', display_name='Gliscor', searchable_by=['Gliscor', 'Stage 1', 'Gliscor'], subtypes=['Stage 1'], collector_number=55, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name', family_id=207, abilities=[Attack(title='Poison Jab', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.FIGHTING: 1}, damage=20, effect=condition_attack(SpecialConditions.POISONED)), Attack(title='Sharp Tail', game_text='Flip a coin. If heads, this attack does 30 damage plus 40 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=flip_bonus(40))])
