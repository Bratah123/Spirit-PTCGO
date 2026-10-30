"""STUB: effect not implemented — do not guess mechanics.
Skitty (EX12 #64): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import (
    important_errands_react,
)

card = PokemonCardDef(guid='f416897b-c42f-545b-96bf-ebe7057b436a', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name', display_name='Skitty', searchable_by=['Skitty', 'Basic', 'Skitty'], subtypes=['Basic'], collector_number=64, set_code='EX12', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=300, abilities=[Attack(title='Important Errands', game_text='Search your deck for a React Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=important_errands_react()), Attack(title='Jump On', game_text='Flip a coin. If heads, this attack does 10 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='+', effect=flip_bonus(20))])
