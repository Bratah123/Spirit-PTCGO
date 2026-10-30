"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition

card = PokemonCardDef(guid='ba04e3e7-f900-5cf1-ab01-91f78e491c41', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name', display_name='Pichu', searchable_by=['Pichu', 'Basic', 'Pichu'], subtypes=['Basic'], collector_number=93, set_code='DP2', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=172, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.', ability_type=AbilityTypes.POKE_POWER, effect=baby_evolution('Pikachu'), activation=Activations.ONCE_PER_TURN, condition=baby_evolution_condition('Pikachu')), Attack(title='Chupi', game_text='Flip a coin. If tails, this attack does nothing.', cost={}, damage=20, effect=flip_or_nothing())])
