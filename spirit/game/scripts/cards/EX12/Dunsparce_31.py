"""STUB: effect not implemented — do not guess mechanics.
Dunsparce (EX12 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    deadlock_named_passive,
    down_draw,
    tripping_turn,
)

card = PokemonCardDef(guid='4dc2ce13-692a-5232-90c7-9501504376b5', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name', display_name='Dunsparce', searchable_by=['Dunsparce', 'Basic', 'Dunsparce'], subtypes=['Basic'], collector_number=31, set_code='EX12', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=206, abilities=[Ability(title='Deadlock', game_text="As long as Dunsparce is your Active Pokémon, your opponent's Dunsparce can't attack.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=deadlock_named_passive('Dunsparce')), Attack(title='Down Draw', game_text='Draw 2 cards from the bottom of your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=down_draw(2)), Attack(title='Tripping Turn', game_text='The Defending Pokémon is now Confused. You may switch Dunsparce with 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 1}, effect=tripping_turn())])
