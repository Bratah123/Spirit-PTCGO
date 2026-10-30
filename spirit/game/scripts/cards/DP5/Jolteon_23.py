"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp5_jolteon_23_lightning_strike,
)

card = PokemonCardDef(guid='8eceda41-6e74-52e8-9bd8-8bb4c498ff0f', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name', display_name='Jolteon', searchable_by=['Jolteon', 'Stage 1', 'Jolteon'], subtypes=['Stage 1'], collector_number=23, set_code='DP5', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name', family_id=133, abilities=[Attack(title='Thunder Fang', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.LIGHTNING: 1}, damage=20, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Lightning Strike', game_text="You may discard 2 Energy attached to Jolteon. If you do, this attack's base damage is 90 instead of 50.", cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=dp5_jolteon_23_lightning_strike())])
