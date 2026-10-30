"""STUB: effect not implemented — do not guess mechanics.
Wailord (EX12 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    reactive_lift_water_retreat_passive,
    rely_on_friends,
)

card = PokemonCardDef(guid='83763ef5-d18b-5585-9006-d9b1b9715163', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name', display_name='Wailord', searchable_by=['Wailord', 'Stage 1', 'Wailord'], subtypes=['Stage 1'], collector_number=14, set_code='EX12', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=4, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name', family_id=320, abilities=[Ability(title='Reactive Lift', game_text='As long as Wailord has any React Energy cards attached to it, the Retreat Cost for each of your Water Pokémon (excluding Pokémon-ex) is 0.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=reactive_lift_water_retreat_passive()), Attack(title='Hypno Splash', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=40, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Rely on Friends', game_text='Does 40 damage plus 10 more damage for each of your Benched Stage 1 Evolved Pokémon.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=rely_on_friends(40, 10))])
