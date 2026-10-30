"""STUB: effect not implemented — do not guess mechanics.
Grimer (EX12 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    ascension,
)

card = PokemonCardDef(guid='8a88298a-ff1c-5f47-99c1-f87866304918', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name', display_name='Grimer', searchable_by=['Grimer', 'Basic', 'Grimer'], subtypes=['Basic'], collector_number=54, set_code='EX12', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=88, abilities=[Attack(title='Ascension', game_text='Search your deck for a card that evolves from Grimer and put it onto Grimer. (This counts as evolving Grimer.) Shuffle your deck afterward.', cost={PokemonTypes.GRASS: 1}, effect=ascension()), Attack(title='Sludge Toss', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
