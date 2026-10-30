"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp5_phione_12_evolution_wish,
)

card = PokemonCardDef(guid='9cf3a5d9-169e-5c7c-8a29-34845d47c1b5', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name', display_name='Phione', searchable_by=['Phione', 'Basic', 'Phione'], subtypes=['Basic'], collector_number=12, set_code='DP5', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=489, abilities=[Attack(title='Evolution Wish', game_text='Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp5_phione_12_evolution_wish()), Attack(title='Water Pulse', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.WATER: 2}, damage=30, effect=condition_attack(SpecialConditions.ASLEEP))])
