"""STUB: effect not implemented — do not guess mechanics.
Magmar (EX12 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import (
    burning_sensation,
    stages_energy_as_fire_passive,
)

card = PokemonCardDef(guid='4156789e-499b-56dd-910c-e2066b23f60b', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name', display_name='Magmar', searchable_by=['Magmar', 'Basic', 'Magmar'], subtypes=['Basic'], collector_number=21, set_code='EX12', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=126, abilities=[Ability(title='Stages of Evolution', game_text='As long as Magmar is an Evolved Pokémon, all Energy attached to Magmar are Fire Energy instead of their usual types.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=stages_energy_as_fire_passive()), Attack(title='Linear Attack', game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 1}, effect=snipe_attack(10, pool='any')), Attack(title='Burning Sensation', game_text='If the Defending Pokémon already has any damage counters on it, the Defending Pokémon is now Burned.', cost={PokemonTypes.FIRE: 3}, damage=40, effect=burning_sensation())])
