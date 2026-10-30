"""STUB: effect not implemented — do not guess mechanics.
Dusknoir (DP7 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_dusknoir_1_damage_even,
    dp7_dusknoir_1_night_spin,
    dp7_dusknoir_1_shadow_command,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='bb9506a1-0f71-50c0-a34e-52dc59e1dc22', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name', display_name='Dusknoir', searchable_by=['Dusknoir', 'Stage 2', 'Dusknoir'], subtypes=['Stage 2'], collector_number=1, set_code='DP7', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name', family_id=355, abilities=[Ability(title='Shadow Command', game_text="Once during your turn (before your attack), you may draw 2 cards. If you have 7 or more cards in your hand, discard a number of cards until you have 6 cards in your hand. Then, put 2 damage counters on Dusknoir. This power can't be used if Dusknoir is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_dusknoir_1_shadow_command(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Damage Even', game_text="Count the number of damage counters on Dusknoir. Put that many damage counters on 1 of your opponent's Pokémon.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, effect=dp7_dusknoir_1_damage_even()), Attack(title='Night Spin', game_text="Prevent all effects of an attack, including damage, done to Dusknoir by your opponent's Pokémon that has 2 or less Energy attached to it during your opponent's next turn.", cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=dp7_dusknoir_1_night_spin())])
