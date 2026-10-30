"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_hitmonlee_100_gut_kick,
)

card = PokemonCardDef(guid='695ec2d3-b6c2-522d-a254-b5f6a4c3d673', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name', display_name='Hitmonlee', searchable_by=['Hitmonlee', 'Basic', 'Hitmonlee'], subtypes=['Basic'], collector_number=100, set_code='DP6', rarity=Rarities.Common, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=106, abilities=[Attack(title='Gut Kick', game_text="If Tyrogue is anywhere under Hitmonlee, you may do 30 damage to any 1 Benched Pokémon instead. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=dp6_hitmonlee_100_gut_kick()), Attack(title='Mega Kick', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=60)])
