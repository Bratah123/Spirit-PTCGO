"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    call_for_family_nidoran,
)

card = PokemonCardDef(guid='dd192e92-9eb6-569b-b2bd-57e39d7bb466', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name', display_name='Nidoran ♀', searchable_by=['Nidoran ♀', 'Basic', 'Nidoran'], subtypes=['Basic'], collector_number=91, set_code='DP2', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=29, abilities=[Attack(title='Call for Family', game_text='Search your deck for Nidoran ♂ or Nidoran ♀ and put it onto your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=call_for_family_nidoran()), Attack(title='Poison Sting', game_text='Flip a coin. If heads, the Defending Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=condition_attack(SpecialConditions.POISONED, flip=True))])
