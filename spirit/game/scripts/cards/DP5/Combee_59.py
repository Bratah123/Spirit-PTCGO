"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import lively_heal_draw
from spirit.game.card_effects.dp import (
    dp5_combee_59_flitter,
)

card = PokemonCardDef(guid='04fece48-72a5-56e9-bf90-03b7d7d65f14', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name', display_name='Combee', searchable_by=['Combee', 'Basic', 'Combee'], subtypes=['Basic'], collector_number=59, set_code='DP5', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=415, abilities=[Attack(title='Honey Scent', game_text='Remove 2 damage counters from 1 of your Pokémon.', cost={PokemonTypes.COLORLESS: 1}, effect=lively_heal_draw()), Attack(title='Flitter', game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. This attack's damage isn't affected by Weakness or Resistance.", cost={PokemonTypes.GRASS: 2}, effect=dp5_combee_59_flitter())])
