"""STUB: effect not implemented — do not guess mechanics.
Bronzor (DP7 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp7_bronzor_55_gyro_swap,
)

card = PokemonCardDef(guid='c860cfe2-17b2-5241-b44c-b2c521f70d1b', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name', display_name='Bronzor', searchable_by=['Bronzor', 'Basic', 'Bronzor'], subtypes=['Basic'], collector_number=55, set_code='DP7', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.FIRE, resistance_amount=20, family_id=436, abilities=[Attack(title='Gyro Swap', game_text="Put a number of damage counters on the Defending Pokémon equal to the number of Colorless Energy in Bronzor's Retreat Cost (after applying effects to the Retreat Cost).", cost={PokemonTypes.PSYCHIC: 1}, effect=dp7_bronzor_55_gyro_swap()), Attack(title='Psyshock', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
