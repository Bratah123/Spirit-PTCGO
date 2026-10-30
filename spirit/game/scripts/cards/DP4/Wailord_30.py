"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_wailord_30_sleeping_pulse_passive,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='5a023115-cb29-57c7-9d19-5ae0a14a72f7', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name', display_name='Wailord', searchable_by=['Wailord', 'Stage 1', 'Wailord'], subtypes=['Stage 1'], collector_number=30, set_code='DP4', rarity=Rarities.Rare, hp=200, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=4, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name', family_id=320, abilities=[Ability(title='Sleeping Pulse', game_text='As long as Wailord remains Asleep between turns, remove 1 damage counter from Wailord.', ability_type=AbilityTypes.POKE_BODY, passive=dp4_wailord_30_sleeping_pulse_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Sink Deep', game_text='If Wailord has any damage counters on it, Wailord is now Asleep.', cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1}, damage=60, effect=condition_attack(SpecialConditions.ASLEEP))])
