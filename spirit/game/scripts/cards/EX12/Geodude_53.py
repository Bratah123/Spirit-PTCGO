"""STUB: effect not implemented — do not guess mechanics.
Geodude (EX12 #53): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    selfdestruct_benches,
)

card = PokemonCardDef(guid='8f025f0d-370f-5e9a-bcf8-be4ed2d5baa9', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name', display_name='Geodude', searchable_by=['Geodude', 'Basic', 'Geodude'], subtypes=['Basic'], collector_number=53, set_code='EX12', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=74, abilities=[Attack(title='Selfdestruct', game_text="Does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.) Geodude does 50 damage to itself.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=selfdestruct_benches(10, 50))])
