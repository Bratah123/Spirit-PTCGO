"""STUB: effect not implemented — do not guess mechanics.
Cascoon (EX12 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    emerge_evolve,
)

card = PokemonCardDef(guid='d7b2f19f-9d6c-5f57-bafd-3a7349de3de3', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name', display_name='Cascoon', searchable_by=['Cascoon', 'Stage 1', 'Cascoon'], subtypes=['Stage 1'], collector_number=30, set_code='EX12', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name', family_id=265, abilities=[Ability(title='Emerge', game_text="Once during your turn (before your attack), if Cascoon is your Active Pokémon, you may flip a coin. If heads, search your deck for a card that evolves from Cascoon and put it onto Cascoon. (This counts as evolving Cascoon.) Shuffle your deck afterward. This power can't be used if Cascoon is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=emerge_evolve(), activation=Activations.ONCE_PER_TURN, usable_from='active'), Attack(title='Tackle', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
