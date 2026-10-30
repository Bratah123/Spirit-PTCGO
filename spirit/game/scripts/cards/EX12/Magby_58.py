"""STUB: effect not implemented — do not guess mechanics.
Magby (EX12 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import baby_evolution_ex7
from spirit.game.card_effects.ex import (
    ignite_if_full_flame,
)

card = PokemonCardDef(guid='ab4f4e06-0fe1-57e9-984b-6d721be19614', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name', display_name='Magby', searchable_by=['Magby', 'Basic', 'Magby'], subtypes=['Basic'], collector_number=58, set_code='EX12', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=240, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Magmar from your hand onto Magby (this counts as evolving Magby) and remove all damage counters from Magby.', ability_type=AbilityTypes.POKE_POWER, effect=baby_evolution_ex7('Magmar')), Attack(title='Ignite', game_text='If Full Flame is in play, the Defending Pokémon is now Burned.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=ignite_if_full_flame())])
