"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_gliscor_5_burning_poison,
    dp6_gliscor_5_pester,
)

card = PokemonCardDef(guid='2054cd68-1089-59f9-9d99-8915ff1983ce', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name', display_name='Gliscor', searchable_by=['Gliscor', 'Stage 1', 'Gliscor'], subtypes=['Stage 1'], collector_number=5, set_code='DP6', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name', family_id=207, abilities=[Attack(title='Burning Poison', game_text='Choose either Burned or Poisoned. The Defending Pokémon is now affected by that Special Condition. You may return Gliscor and all cards attached to it to your hand.', cost={}, effect=dp6_gliscor_5_burning_poison()), Attack(title='Pester', game_text='If the Defending Pokémon is affected by a Special Condition, this attack does 40 damage plus 40 more damage.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=dp6_gliscor_5_pester())])
