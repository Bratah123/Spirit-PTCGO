"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp5_manectric_40_volt_crush,
)

card = PokemonCardDef(guid='89194065-8d01-5f15-b991-2c2b3a923853', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name', display_name='Manectric', searchable_by=['Manectric', 'Stage 1', 'Manectric'], subtypes=['Stage 1'], collector_number=40, set_code='DP5', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name', family_id=309, abilities=[Attack(title='Thunder Wave', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.LIGHTNING: 1}, damage=30, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Volt Crush', game_text='Flip a coin. If heads, discard an Energy attached to Manectric and this attack does 40 damage plus 30 more damage.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=dp5_manectric_40_volt_crush())])
