"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_slowpoke_82_tumble_over,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='7384cdc0-db40-5991-929b-c51223e0b279', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name', display_name='Slowpoke', searchable_by=['Slowpoke', 'Basic', 'Slowpoke'], subtypes=['Basic'], collector_number=82, set_code='DP4', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, family_id=79, abilities=[Attack(title='Rest', game_text='Remove all Special Conditions and 3 damage counters from Slowpoke. Slowpoke is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Tumble Over', game_text="Slowpoke can't attack during your next turn.", cost={PokemonTypes.WATER: 1}, damage=20, effect=dp4_slowpoke_82_tumble_over())])
