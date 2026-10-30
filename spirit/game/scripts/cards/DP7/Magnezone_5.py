"""STUB: effect not implemented — do not guess mechanics.
Magnezone (DP7 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.dp import (
    dp7_magnezone_5_magnetic_search,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='c4c74e14-81c6-5634-95f7-06ed349c5572', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name', display_name='Magnezone', searchable_by=['Magnezone', 'Stage 2', 'Magnezone'], subtypes=['Stage 2'], collector_number=5, set_code='DP7', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name', family_id=81, abilities=[Ability(title='Magnetic Search', game_text="Once during your turn (before your attack), you may search your deck for a Lightning or Metal Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Magnezone is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_magnezone_5_magnetic_search(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Speed Shot', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, effect=snipe_attack(30, pool='any')), Attack(title='Crush Volt', game_text='Discard an Energy attached to Magnezone.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=80, effect=self_energy_discard_attack(count=1, then_damage=80))])
