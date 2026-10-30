"""STUB: effect not implemented — do not guess mechanics.
Voltorb (DP7 #SH3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp7_voltorb_sh3_charge_beam,
)
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='cb9f595f-a07c-57ef-bad9-45f16c2fcc44', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name', display_name='Voltorb', searchable_by=['Voltorb', 'Basic', 'Voltorb'], subtypes=['Basic'], collector_number=106, set_code='DP7', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=100, abilities=[Attack(title='Fastball', game_text="Choose 1 of your opponent's Pokémon. Flip a coin. If heads, this attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 1}, effect=snipe_attack(20, pool='bench')), Attack(title='Charge Beam', game_text='Search your discard pile for a Lightning Energy card and attach it to Voltorb.', cost={PokemonTypes.LIGHTNING: 1}, damage=10, effect=dp7_voltorb_sh3_charge_beam()), Attack(title='Thundershock', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
