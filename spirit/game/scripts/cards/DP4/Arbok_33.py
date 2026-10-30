"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='6fcf5d0b-afde-5fe4-ab71-5f842dcc7c10', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name', display_name='Arbok', searchable_by=['Arbok', 'Stage 1', 'Arbok'], subtypes=['Stage 1'], collector_number=33, set_code='DP4', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name', family_id=23, abilities=[Attack(title='Deadly Poison', game_text='If the Defending Pokémon is Poisoned, this attack does 10 damage plus 40 more damage. If the Defending Pokémon is not Poisoned, that Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 1}, damage=10, damage_operator='+', effect=condition_attack(SpecialConditions.POISONED)), Attack(title='Wrap', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 3}, damage=50, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
