"""STUB: effect not implemented — do not guess mechanics.
Lairon (EX12 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    rest_full_asleep,
)

card = PokemonCardDef(guid='9a469c54-cb4b-588f-ba01-3933d0af8432', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name', display_name='Lairon', searchable_by=['Lairon', 'Stage 1', 'Lairon'], subtypes=['Stage 1'], collector_number=38, set_code='EX12', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name', family_id=304, abilities=[Attack(title='Rest', game_text='Remove all Special Conditions and 5 damage counters (all if there are less than 5) from Lairon. Lairon is now Asleep.', cost={PokemonTypes.COLORLESS: 2}, effect=rest_full_asleep(5)), Attack(title='Body Slam', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
