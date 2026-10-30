"""STUB: effect not implemented — do not guess mechanics.
Bidoof (DP7 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp7_bidoof_54_self_abandonment,
)

card = PokemonCardDef(guid='137e3577-e7f1-5ba4-9b56-4860464773b4', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name', display_name='Bidoof', searchable_by=['Bidoof', 'Basic', 'Bidoof'], subtypes=['Basic'], collector_number=54, set_code='DP7', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=399, abilities=[Attack(title='Yawn', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Self-abandonment', game_text='Flip a coin. If heads, this attack does 30 damage to the Defending Pokémon. If tails, Bidoof does 10 damage to itself.', cost={PokemonTypes.COLORLESS: 1}, effect=dp7_bidoof_54_self_abandonment())])
