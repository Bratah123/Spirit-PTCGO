"""STUB: effect not implemented — do not guess mechanics.
Dusknoir (DP7 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_dusknoir_17_darkness_mist,
    dp7_dusknoir_17_spirit_pulse_passive,
)

card = PokemonCardDef(guid='9bc2f7ee-2e2d-5bb4-a679-2e0b02ef3fb4', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name', display_name='Dusknoir', searchable_by=['Dusknoir', 'Stage 2', 'Dusknoir'], subtypes=['Stage 2'], collector_number=17, set_code='DP7', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name', family_id=355, abilities=[Ability(title='Spirit Pulse', game_text="As long as Dusknoir is your Active Pokémon, put 1 damage counter on each of your opponent's Pokémon that has any Energy attached to it between turns.", ability_type=AbilityTypes.POKE_BODY, passive=dp7_dusknoir_17_spirit_pulse_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Darkness Mist', game_text='If the Defending Pokémon already has 2 or more damage counters on it, this attack does 60 damage plus 20 more damage.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp7_dusknoir_17_darkness_mist())])
