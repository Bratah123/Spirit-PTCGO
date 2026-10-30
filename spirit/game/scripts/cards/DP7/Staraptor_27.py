"""STUB: effect not implemented — do not guess mechanics.
Staraptor (DP7 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import magma_ring_no_retreat
from spirit.game.card_effects.dp import (
    dp7_staraptor_27_protect_wing_passive,
    dp7_staraptor_27_strong_breeze,
)

card = PokemonCardDef(guid='3cb656c9-c8e9-5817-9337-a51367a83217', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name', display_name='Staraptor', searchable_by=['Staraptor', 'Stage 2', 'Staraptor'], subtypes=['Stage 2'], collector_number=27, set_code='DP7', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name', family_id=396, abilities=[Ability(title='Protect Wing', game_text="As long as Staraptor is your Active Pokémon, any damage done by attacks from your opponent's Stage 2 Evolved Pokémon is reduced by 20 (after applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, passive=dp7_staraptor_27_protect_wing_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Strong Breeze', game_text="Flip a coin. If heads, put 1 of your opponent's Benched Pokémon and all cards attached to it on top of your opponent's deck. Your opponent shuffles his or her deck afterward.", cost={PokemonTypes.COLORLESS: 1}, effect=dp7_staraptor_27_strong_breeze()), Attack(title='Clutch', game_text="The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 3}, damage=60, effect=magma_ring_no_retreat())])
