"""STUB: effect not implemented — do not guess mechanics.
Miltank (DP7 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.dp import (
    dp7_miltank_44_energy_milk,
)

card = PokemonCardDef(guid='7a76ca0c-6751-53cb-8b07-2e46beeeee7b', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name', display_name='Miltank', searchable_by=['Miltank', 'Basic', 'Miltank'], subtypes=['Basic'], collector_number=44, set_code='DP7', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=241, abilities=[Attack(title='Collect', game_text='Draw a card.', cost={PokemonTypes.COLORLESS: 1}, effect=draw_attack(1)), Attack(title='Energy Milk', game_text='Flip a coin until you get tails. For each heads, remove 2 damage counters from 1 of your Pokémon.', cost={PokemonTypes.COLORLESS: 1}, effect=dp7_miltank_44_energy_milk()), Attack(title='Stomp', game_text='Flip a coin. If heads, this attack does 20 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='+', effect=flip_bonus(20))])
