"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_castformrainform_49_temperament,
)

card = PokemonCardDef(guid='eb6208e9-4b91-501a-b667-c25ff5b2846d', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.CastformRainForm.Name', display_name='Castform Rain Form', searchable_by=['Castform Rain Form', 'Basic', 'CastformRainForm'], subtypes=['Basic'], collector_number=49, set_code='DP6', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=351, abilities=[Ability(title='Temperament', game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform Rain Form. (Any cards attached to Castform Rain Form, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) Shuffle Castform Rain Form back into your deck. You can't use more than 1 Temperament Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_castformrainform_49_temperament(), activation=Activations.ONCE_PER_TURN), Attack(title='Water Pulse', game_text='The defending Pokémon is now Asleep.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.ASLEEP))])
