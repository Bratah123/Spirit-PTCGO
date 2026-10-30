"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    ghastly_sound_no_supporters,
)

card = PokemonCardDef(guid='c7a31752-db51-547b-91aa-b0acaf6a8149', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name', display_name='Croagunk', searchable_by=['Croagunk', 'Basic', 'Croagunk'], subtypes=['Basic'], collector_number=78, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=453, abilities=[Attack(title='Ghastly Sound', game_text="Flip a coin. If heads, your opponent can't play any Supporter cards from his or her hand during his or her next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=ghastly_sound_no_supporters()), Attack(title='Finger Poke', game_text='Flip a coin. If heads, the Defending Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 2}, damage=20, effect=condition_attack(SpecialConditions.POISONED, flip=True))])
