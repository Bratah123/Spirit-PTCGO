"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_luxray_8_plasma,
    dp6_luxray_8_rivalry,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(guid='a63384ed-5e61-5191-a276-f2683beaf653', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name', display_name='Luxray', searchable_by=['Luxray', 'Stage 2', 'Luxray'], subtypes=['Stage 2'], collector_number=8, set_code='DP6', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name', family_id=403, abilities=[Ability(title='Rivalry', game_text="If your opponent has any Pokémon LV.X in play, each of Luxray's attacks does 50 more damage to the Active Pokémon (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=dp6_luxray_8_rivalry(), activation=Activations.ONCE_PER_TURN), Attack(title='Plasma', game_text='Search your discard pile for a Lightning Energy card and attach it to Luxray.', cost={PokemonTypes.COLORLESS: 2}, damage=40, effect=dp6_luxray_8_plasma()), Attack(title='Shock Bolt', game_text='Discard all Lightning Energy attached to Luxray.', cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=100, effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.LIGHTNING, then_damage=100))])
