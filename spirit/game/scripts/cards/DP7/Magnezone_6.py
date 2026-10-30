"""STUB: effect not implemented — do not guess mechanics.
Magnezone (DP7 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_magnezone_6_gyro_ball,
    dp7_magnezone_6_super_connectivity,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='ef59c08a-af60-5081-ba9f-0f69b272e837', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name', display_name='Magnezone', searchable_by=['Magnezone', 'Stage 2', 'Magnezone'], subtypes=['Stage 2'], collector_number=6, set_code='DP7', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name', family_id=81, abilities=[Ability(title='Super Connectivity', game_text="Once during your turn (before your attack), you may search your discard pile for a Lightning or Metal Energy card and attach it to your Active Pokémon. Then, put 1 damage counter on that Pokémon. This power can't be used if Magnezone is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_magnezone_6_super_connectivity(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Gyro Ball', game_text='You may switch Magnezone with 1 of your Benched Pokémon. If you do, your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp7_magnezone_6_gyro_ball())])
