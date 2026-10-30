"""STUB: effect not implemented — do not guess mechanics.
Girafarig (EX12 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    disorder_confuse_if_special_energy,
    foresight_reorder,
    rear_sensor_passive,
)

card = PokemonCardDef(guid='c8737ac4-fb67-51d8-a1fa-e0e8cecf2a66', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name', display_name='Girafarig', searchable_by=['Girafarig', 'Basic', 'Girafarig'], subtypes=['Basic'], collector_number=16, set_code='EX12', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=203, abilities=[Ability(title='Rear Sensor', game_text="Each player's Active Basic Pokémon (excluding Pokémon-ex) can't use any Poké-Powers.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=rear_sensor_passive()), Attack(title='Foresight', game_text="Look at the top 5 cards on either player's deck and put them back on top of that player's deck in any order you like.", cost={PokemonTypes.COLORLESS: 1}, effect=foresight_reorder(5)), Attack(title='Disorder', game_text='If the Defending Pokémon has any Special Energy cards attached to it, the Defending Pokémon is now Confused.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=disorder_confuse_if_special_energy(20))])
