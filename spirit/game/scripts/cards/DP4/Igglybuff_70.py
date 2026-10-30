"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_igglybuff_70_inquire,
)
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition

card = PokemonCardDef(guid='88b4dc36-e781-51f6-9fe9-e28c2724fe0a', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name', display_name='Igglybuff', searchable_by=['Igglybuff', 'Basic', 'Igglybuff'], subtypes=['Basic'], collector_number=70, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=174, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Jigglypuff from your hand onto Igglybuff (this counts as evolving Igglybuff) and remove all damage counters from Igglybuff.', ability_type=AbilityTypes.POKE_POWER, effect=baby_evolution('Jigglypuff'), activation=Activations.ONCE_PER_TURN, condition=baby_evolution_condition('Jigglypuff')), Attack(title='Inquire', game_text="Draw a card. If you didn't play any Supporter card from your hand during this turn, draw 2 more cards.", cost={}, effect=dp4_igglybuff_70_inquire())])
