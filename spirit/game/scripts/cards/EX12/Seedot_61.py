"""STUB: effect not implemented — do not guess mechanics.
Seedot (EX12 #61): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    continuous_tumble,
    drawup_power_energy,
)

card = PokemonCardDef(guid='bf5bbefd-51d4-566a-8591-8531662c3ea2', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name', display_name='Seedot', searchable_by=['Seedot', 'Basic', 'Seedot'], subtypes=['Basic'], collector_number=61, set_code='EX12', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=273, abilities=[Attack(title='Drawup Power', game_text='Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=drawup_power_energy()), Attack(title='Continuous Tumble', game_text='Flip a coin until you get tails. This attack does 10 damage times the number of heads.', cost={PokemonTypes.GRASS: 1}, damage=10, damage_operator='x', effect=continuous_tumble(10))])
