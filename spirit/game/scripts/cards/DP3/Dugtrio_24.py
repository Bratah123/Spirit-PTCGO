"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_dugtrio_24_pit_trap,
)
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='eaaface5-70d1-562d-ad8a-4b74c43a6833', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name', display_name='Dugtrio', searchable_by=['Dugtrio', 'Stage 1', 'Dugtrio'], subtypes=['Stage 1'], collector_number=24, set_code='DP3', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name', family_id=50, abilities=[Attack(title='Dig Trap', game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of an attack, including damage, done to Dugtrio during your opponent's next turn. If Dugtrio is your Active Pokémon at the end of your opponent's next turn, put 6 damage counters on 1 of your opponent's Benched Pokémon.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, effect=flip_or_nothing()), Attack(title='Pit Trap', game_text='Your opponent flips a coin. If tails, this attack does 50 damage plus 50 more damage.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=50, damage_operator='+', effect=dp3_dugtrio_24_pit_trap())])
