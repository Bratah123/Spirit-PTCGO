"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import magma_ring_no_retreat
from spirit.game.card_effects.dp import (
    dp6_cradily_21_drain_down,
)

card = PokemonCardDef(guid='31384d96-a4ef-5d3f-99bd-b23f353ba5c0', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name', display_name='Cradily', searchable_by=['Cradily', 'Stage 2', 'Cradily'], subtypes=['Stage 2'], collector_number=21, set_code='DP6', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name', family_id=345, abilities=[Attack(title='Drain Down', game_text="Before doing damage, you may switch 1 of the Defending Pokémon with 1 of your opponent's Benched Pokémon. If you do, this attack does 30 damage to the new Defending Pokémon. If the Defending Pokémon would be Knocked Out by this attack, you may remove all damage counters from Cradily.", cost={PokemonTypes.GRASS: 1}, damage=30, effect=dp6_cradily_21_drain_down()), Attack(title='Acid', game_text="The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=magma_ring_no_retreat())])
