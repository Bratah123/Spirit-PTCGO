"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_yanmega_17_pursue_and_turn,
    dp6_yanmega_17_sonic_wave,
)

card = PokemonCardDef(guid='6a1fda79-6eb1-5329-a695-a31377a71cdc', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name', display_name='Yanmega', searchable_by=['Yanmega', 'Stage 1', 'Yanmega'], subtypes=['Stage 1'], collector_number=17, set_code='DP6', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name', family_id=193, abilities=[Attack(title='Sonic Wave', game_text="Does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.", cost={}, damage=10, effect=dp6_yanmega_17_sonic_wave()), Attack(title='Pursue and Turn', game_text='If the Defending Pokémon already has 2 or more damage counters on it, this attack does 60 damage plus 20 more damage and switch Yanmega with 1 of your Benched Pokémon.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp6_yanmega_17_pursue_and_turn())])
