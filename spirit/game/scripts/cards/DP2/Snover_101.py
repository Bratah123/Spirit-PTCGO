"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    curiosity_look_hand,
)
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='481347be-7e9f-5a2b-a103-c5cd4b4a58df', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name', display_name='Snover', searchable_by=['Snover', 'Basic', 'Snover'], subtypes=['Basic'], collector_number=101, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIRE, family_id=459, abilities=[Attack(title='Curiosity', game_text="Look at your opponent's hand.", cost={}, effect=curiosity_look_hand()), Attack(title='Snowball Fight', game_text='Flip a coin. If tails, Snover does 10 damage to itself.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=recoil_attack(10, damage=30))])
