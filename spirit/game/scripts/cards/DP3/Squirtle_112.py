"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_squirtle_112_aqua_tail,
)

card = PokemonCardDef(guid='9306d2e6-02c5-5f73-8178-bf98fd6922d7', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name', display_name='Squirtle', searchable_by=['Squirtle', 'Basic', 'Squirtle'], subtypes=['Basic'], collector_number=112, set_code='DP3', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=7, abilities=[Attack(title='Bubble', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={}, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Aqua Tail', game_text='Flip a coin for each Water Energy attached to Squirtle. This attack does 20 damage plus 10 more damage for each heads.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp3_squirtle_112_aqua_tail())])
