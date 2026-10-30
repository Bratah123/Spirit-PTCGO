"""STUB: effect not implemented — do not guess mechanics.
Banette ex (EX12 #85): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    shadow_chant,
    shady_move_counter,
)

card = PokemonCardDef(guid='9d2e7fd3-833e-5e52-be05-3726655de999', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Banetteex.Name', display_name='Banette ex', searchable_by=['Banette ex', 'Stage 1', 'ex', 'Banetteex'], subtypes=['Stage 1', 'ex'], collector_number=85, set_code='EX12', rarity=Rarities.RareHoloEX, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name', family_id=353, abilities=[Ability(title='Shady Move', game_text="Once during your turn (before your attack), if Banette ex is your Active Pokémon, you may move 1 damage counter from either player's Pokémon to another Pokémon (yours or your opponent's). This power can't be used if Banette ex is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=shady_move_counter(), activation=Activations.ONCE_PER_TURN, usable_from='active'), Attack(title='Shadow Chant', game_text="Does 30 damage plus 10 more damage for each Supporter card in your discard pile. You can't add more than 60 damage in this way.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=shadow_chant(30, 10, 60))])
