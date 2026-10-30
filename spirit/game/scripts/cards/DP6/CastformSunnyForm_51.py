"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_castformsunnyform_51_temperament,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(guid='c935b04c-d1a4-51cc-afc9-d0a69f6dbc6f', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.CastformSunnyForm.Name', display_name='Castform Sunny Form', searchable_by=['Castform Sunny Form', 'Basic', 'CastformSunnyForm'], subtypes=['Basic'], collector_number=51, set_code='DP6', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=351, abilities=[Ability(title='Temperament', game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform Sunny Form. (Any cards attached to Castform Sunny Form, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) Shuffle Castform Sunny Form back into your deck. You can't use more than 1 Temperament Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_castformsunnyform_51_temperament(), activation=Activations.ONCE_PER_TURN), Attack(title='Ember', game_text='Discard a Fire Energy attached to Castform Sunny Form.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=self_energy_discard_attack(count=1, then_damage=40))])
