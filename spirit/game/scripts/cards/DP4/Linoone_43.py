"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_linoone_43_overrun,
    dp4_linoone_43_switcheroo,
)

card = PokemonCardDef(guid='d803ef8b-4df5-55f5-a7f6-624a41c2198c', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name', display_name='Linoone', searchable_by=['Linoone', 'Stage 1', 'Linoone'], subtypes=['Stage 1'], collector_number=43, set_code='DP4', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name', family_id=263, abilities=[Attack(title='Switcheroo', game_text="Move a Pokémon Tool card attached to 1 of your opponent's Pokémon to another of your opponent's Pokémon (excluding Pokémon that already has a Pokémon Tool attached to it). (If an effect of this attack is prevented, this attack does nothing.)", cost={}, effect=dp4_linoone_43_switcheroo()), Attack(title='Overrun', game_text="Does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 3}, damage=30, effect=dp4_linoone_43_overrun())])
