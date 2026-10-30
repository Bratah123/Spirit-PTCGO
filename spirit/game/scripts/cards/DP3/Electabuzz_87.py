"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_electabuzz_87_thunder,
)

card = PokemonCardDef(guid='1fbfe447-e4a8-54a6-a5a9-8d45ecd30b44', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name', display_name='Electabuzz', searchable_by=['Electabuzz', 'Basic', 'Electabuzz'], subtypes=['Basic'], collector_number=87, set_code='DP3', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=125, abilities=[Attack(title='Thundershock', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.LIGHTNING: 1}, damage=10, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Thunder', game_text='Flip a coin. If tails, Electabuzz does 30 damage to itself.', cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp3_electabuzz_87_thunder())])
