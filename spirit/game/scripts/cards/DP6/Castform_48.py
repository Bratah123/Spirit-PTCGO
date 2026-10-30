"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_castform_48_temperament,
    dp6_castform_48_weather_ball,
)

card = PokemonCardDef(guid='c7c7915f-d4d0-5994-8e4d-15647c5317bb', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name', display_name='Castform', searchable_by=['Castform', 'Basic', 'Castform'], subtypes=['Basic'], collector_number=48, set_code='DP6', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=351, abilities=[Ability(title='Temperament', game_text="Once during your turn (before your attack), you may search your deck for any Castform and switch it with Castform. (Any cards attached to Castform, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Castform on top of your deck. Shuffle your deck afterward. You can't use more than 1 Temperament Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_castform_48_temperament(), activation=Activations.ONCE_PER_TURN), Attack(title='Weather Ball', game_text='If you have a Stadium card in play, remove 3 damage counters from Castform. If your opponent has a Stadium card in play, this attack does 30 damage plus 30 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=dp6_castform_48_weather_ball())])
