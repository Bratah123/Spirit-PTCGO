"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    inviting_bell,
)
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition

card = PokemonCardDef(guid='b23f9c98-c001-5319-9e6e-50d2b3341b40', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Chingling.Name', display_name='Chingling', searchable_by=['Chingling', 'Basic', 'Chingling'], subtypes=['Basic'], collector_number=42, set_code='DP2', rarity=Rarities.Uncommon, hp=40, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=433, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Chimecho from your hand onto Chingling (this counts as evolving Chingling) and remove all damage counters from Chingling.', ability_type=AbilityTypes.POKE_POWER, effect=baby_evolution('Chimecho'), activation=Activations.ONCE_PER_TURN, condition=baby_evolution_condition('Chimecho')), Attack(title='Inviting Bell', game_text='Search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={}, effect=inviting_bell())])
