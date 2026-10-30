"""STUB: effect not implemented — do not guess mechanics.
Pinsir (EX12 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    cry_for_help,
    overhead_toss,
    shining_horn_solo_passive,
)

card = PokemonCardDef(guid='720548ea-7f42-5bdd-a4df-77e90b32be12', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name', display_name='Pinsir', searchable_by=['Pinsir', 'Basic', 'Pinsir'], subtypes=['Basic'], collector_number=24, set_code='EX12', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=127, abilities=[Ability(title='Shining Horn', game_text="As long as Pinsir is the only Pokémon you have in play, your opponent's Basic Pokémon can't attack.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=shining_horn_solo_passive()), Attack(title='Cry for Help', game_text='Search your deck for a Grass Pokémon (excluding Pokémon-ex), show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=cry_for_help(PokemonTypes.GRASS)), Attack(title='Overhead Toss', game_text="Does 20 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=overhead_toss(30, 20))])
