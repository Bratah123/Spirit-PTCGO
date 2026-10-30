"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.ex import (
    paste_energy_to_delta,
)

card = PokemonCardDef(guid='856d2e66-75d3-5c72-8d09-3dd5d1fe9357', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name', display_name='Pichu δ', searchable_by=['Pichu δ', 'Basic', 'Pichu'], subtypes=['Basic'], collector_number=76, set_code='EX13', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=172, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.', ability_type=AbilityTypes.POKE_POWER, activation=Activations.ONCE_PER_TURN, condition=baby_evolution_condition('Pikachu'), effect=baby_evolution('Pikachu')), Attack(title='Paste', game_text='Search your discard pile for an Energy card and attach it to 1 of your Pokémon that has δ on its card.', cost={PokemonTypes.COLORLESS: 1}, effect=paste_energy_to_delta())])
