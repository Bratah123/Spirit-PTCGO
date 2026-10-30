"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_venomoth_73_dangerous_scales,
    dp3_venomoth_73_disturbance_dive,
)

card = PokemonCardDef(guid='04df4de4-24b0-5f84-b34a-3fb272329334', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name', display_name='Venomoth', searchable_by=['Venomoth', 'Stage 1', 'Venomoth'], subtypes=['Stage 1'], collector_number=73, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name', family_id=48, abilities=[Ability(title='Dangerous Scales', game_text="If Venomoth is your Active Pokémon and is damaged by an opponent's attack (even if Venomoth is Knocked Out), the Attacking Pokémon is now Asleep and Poisoned.", ability_type=AbilityTypes.POKE_BODY, effect=dp3_venomoth_73_dangerous_scales(), activation=Activations.ONCE_PER_TURN), Attack(title='Disturbance Dive', game_text="Prevent all effects of an attack, excluding damage, done to Venomoth during your opponent's next turn.", cost={PokemonTypes.GRASS: 2}, damage=50, effect=dp3_venomoth_73_disturbance_dive())])
