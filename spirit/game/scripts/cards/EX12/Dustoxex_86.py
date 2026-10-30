"""STUB: effect not implemented — do not guess mechanics.
Dustox ex (EX12 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import silver_wind
from spirit.game.card_effects.ex import (
    safeguard_ex_passive,
)

card = PokemonCardDef(guid='1e4df7db-e0cb-5d1a-958b-7027ab443162', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dustoxex.Name', display_name='Dustox ex', searchable_by=['Dustox ex', 'Stage 2', 'ex', 'Dustoxex'], subtypes=['Stage 2', 'ex'], collector_number=86, set_code='EX12', rarity=Rarities.RareHoloEX, hp=140, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name', family_id=265, abilities=[Ability(title='Safeguard', game_text="Prevent all effects of attacks, including damage, done to Dustox ex by your opponent's Pokémon-ex.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=safeguard_ex_passive()), Attack(title='Silver Wind', game_text='During your next turn, if an attack does damage to the Defending Pokémon (after applying Weakness and Resistance), that attack does 30 more damage.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=silver_wind()), Attack(title='Cutting Wind', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=70)])
