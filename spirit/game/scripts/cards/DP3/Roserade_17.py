"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp3_roserade_17_magical_leaf,
)

card = PokemonCardDef(guid='e4bc84df-be83-572c-9e55-99f55015eb30', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name', display_name='Roserade', searchable_by=['Roserade', 'Stage 1', 'Roserade'], subtypes=['Stage 1'], collector_number=17, set_code='DP3', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name', family_id=315, abilities=[Attack(title='Sleep Poison', game_text='The Defending Pokémon is now Asleep and Poisoned.', cost={PokemonTypes.GRASS: 1}, damage=20, effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED)), Attack(title='Magical Leaf', game_text='Flip a coin. If heads, this attack does 40 damage plus 30 more damage and remove 3 damage counters from Roserade.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=dp3_roserade_17_magical_leaf())])
