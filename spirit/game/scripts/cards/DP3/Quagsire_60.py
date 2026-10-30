"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.dp import (
    dp3_quagsire_60_aqua_healing,
)

card = PokemonCardDef(guid='d1a643f0-0d94-578d-a17e-58358a3803b9', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name', display_name='Quagsire', searchable_by=['Quagsire', 'Stage 1', 'Quagsire'], subtypes=['Stage 1'], collector_number=60, set_code='DP3', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name', family_id=194, abilities=[Ability(title='Aqua Healing', game_text='Once during your turn (before your attack), if Quagsire is your Active Pokémon and the Defending Pokémon has any Water Energy attached to it, you may remove 3 damage counters from Quagsire.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_quagsire_60_aqua_healing(), activation=Activations.ONCE_PER_TURN), Attack(title='Muddy Water', game_text="Does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=snipe_attack(20))])
