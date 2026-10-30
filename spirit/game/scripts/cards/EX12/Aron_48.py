"""STUB: effect not implemented — do not guess mechanics.
Aron (EX12 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    self_charge_metal_from_hand,
)

card = PokemonCardDef(guid='5a9479cc-c6df-53f8-a0c4-18cd721a2617', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name', display_name='Aron', searchable_by=['Aron', 'Basic', 'Aron'], subtypes=['Basic'], collector_number=48, set_code='EX12', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.GRASS, family_id=304, abilities=[Attack(title='Self Charge', game_text='Attach a Metal Energy card from your hand to Aron.', cost={PokemonTypes.COLORLESS: 1}, effect=self_charge_metal_from_hand()), Attack(title='Headbutt', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20)])
