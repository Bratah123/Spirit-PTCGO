"""STUB: effect not implemented — do not guess mechanics.
Solrock (EX12 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.ex import (
    call_for_lunatone,
    luna_shade_passive,
)

card = PokemonCardDef(guid='9cef0127-3a66-5c89-bb04-3bb73065658b', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name', display_name='Solrock', searchable_by=['Solrock', 'Basic', 'Solrock'], subtypes=['Basic'], collector_number=25, set_code='EX12', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=338, abilities=[Ability(title='Luna Shade', game_text="As long as you have Lunatone in play, each player's Colorless Pokémon (excluding Pokémon-ex) can't use any Poké-Powers.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=luna_shade_passive()), Attack(title='Call for Family', game_text='Search your deck for a Lunatone and put it onto your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=call_for_lunatone()), Attack(title='Hyper Beam', game_text='Flip a coin. If heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.FIGHTING: 1}, effect=discard_opponent_energy_attack(1, flip=True))])
