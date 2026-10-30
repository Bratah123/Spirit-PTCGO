"""STUB: effect not implemented — do not guess mechanics.
Onix (DP7 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp7_onix_69_harden,
)

card = PokemonCardDef(guid='e29cee0e-15b2-593d-88e5-53c6bc74f287', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name', display_name='Onix', searchable_by=['Onix', 'Basic', 'Onix'], subtypes=['Basic'], collector_number=69, set_code='DP7', rarity=Rarities.Common, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.GRASS, family_id=95, abilities=[Attack(title='Harden', game_text="During your opponent's next turn, if Onix would be damaged by an attack, prevent that attack's damage done to Onix if that damage is 40 or less.", cost={PokemonTypes.COLORLESS: 1}, effect=dp7_onix_69_harden()), Attack(title='Bind', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=30, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
