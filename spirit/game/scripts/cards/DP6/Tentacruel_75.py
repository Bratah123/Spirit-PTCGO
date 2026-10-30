"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_tentacruel_75_dangerous_poison,
    dp6_tentacruel_75_tentacle_strike,
)

card = PokemonCardDef(guid='166d08ad-77b9-5859-9f29-75f32e4ef36f', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name', display_name='Tentacruel', searchable_by=['Tentacruel', 'Stage 1', 'Tentacruel'], subtypes=['Stage 1'], collector_number=75, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name', family_id=72, abilities=[Attack(title='Tentacle Strike', game_text="Search your opponent's discard pile for up to 2 Energy cards and attach them to any of your opponent's Pokémon in any way you like. For each Energy card attached in this way, this attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={}, effect=dp6_tentacruel_75_tentacle_strike()), Attack(title='Dangerous Poison', game_text='If Tentacruel has less Energy attached to it than the Defending Pokémon, the Defending Pokémon is now Paralyzed and Poisoned.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp6_tentacruel_75_dangerous_poison())])
