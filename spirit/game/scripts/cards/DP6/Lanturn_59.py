"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_lanturn_59_aqua_bolt,
    dp6_lanturn_59_energy_split,
)

card = PokemonCardDef(guid='384d9599-e247-5117-a02e-377f11ad87d6', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name', display_name='Lanturn', searchable_by=['Lanturn', 'Stage 1', 'Lanturn'], subtypes=['Stage 1'], collector_number=59, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name', family_id=170, abilities=[Attack(title='Energy Split', game_text="This attack does 30 damage to each of your opponent's Pokémon that has any Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 1}, effect=dp6_lanturn_59_energy_split()), Attack(title='Aqua Bolt', game_text='Does 60 damage plus 10 more damage for each Water Energy attached to Lanturn.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp6_lanturn_59_aqua_bolt())])
