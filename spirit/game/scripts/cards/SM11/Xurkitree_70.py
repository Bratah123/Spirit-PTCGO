from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm11 import three_mirrors

card = PokemonCardDef(guid='6f05bd1a-6517-578f-86b9-884a02974006', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Xurkitree.Name', display_name='Xurkitree', searchable_by=['Xurkitree', 'Basic', 'Ultra Beast', 'Xurkitree'], subtypes=['Basic', 'Ultra Beast'], collector_number=70, set_code='SM11', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=796, abilities=[Attack(title='Three Mirrors', game_text='If your opponent has exactly 3 Prize cards remaining, this attack does 90 more damage.', cost={PokemonTypes.LIGHTNING: 1}, damage=30, damage_operator='+', effect=three_mirrors), Attack(title='Signal Beam', game_text="Your opponent's Active Pokémon is now Confused.", cost={PokemonTypes.LIGHTNING: 2}, damage=50, effect=condition_attack(SpecialConditions.CONFUSED))])
