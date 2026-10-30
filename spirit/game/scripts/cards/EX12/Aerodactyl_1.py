"""STUB: effect not implemented — do not guess mechanics.
Aerodactyl (EX12 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    power_blow,
    prevent_ex_attacks_next_turn,
    react_protection_per,
)

card = PokemonCardDef(guid='d4d278ae-2bac-5771-aeac-cbbbc8f17d2c', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name', display_name='Aerodactyl', searchable_by=['Aerodactyl', 'Stage 1', 'Aerodactyl'], subtypes=['Stage 1'], collector_number=1, set_code='EX12', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name', family_id=142, abilities=[Ability(title='Reactive Protection', game_text="Any damage done to Aerodactyl by attacks from your opponent's Pokémon is reduced by 10 for each React Energy card attached to Aerodactyl (after applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=react_protection_per(10)), Attack(title='Power Blow', game_text='Does 10 damage plus 10 more damage for each Energy attached to Aerodactyl.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=power_blow()), Attack(title='Speed Stroke', game_text="During your opponent's next turn, prevent all effects, including damage, done to Aerodactyl by attacks from your opponent's Pokémon-ex.", cost={PokemonTypes.COLORLESS: 3}, damage=40, effect=prevent_ex_attacks_next_turn())])
