"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_smoochum_67_psykiss,
)
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition

card = PokemonCardDef(guid='ff106a12-09ea-5b3d-8706-ccf36c1c8056', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name', display_name='Smoochum', searchable_by=['Smoochum', 'Basic', 'Smoochum'], subtypes=['Basic'], collector_number=67, set_code='DP3', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=238, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Jynx from your hand onto Smoochum (this counts as evolving Smoochum) and remove all damage counters from Smoochum.', ability_type=AbilityTypes.POKE_POWER, effect=baby_evolution('Jynx'), activation=Activations.ONCE_PER_TURN, condition=baby_evolution_condition('Jynx')), Attack(title='Psykiss', game_text="Flip a coin. If heads, choose a Special Energy card attached to 1 of your opponent's Pokémon and have your opponent shuffle that card into his or her deck.", cost={}, effect=dp3_smoochum_67_psykiss())])
