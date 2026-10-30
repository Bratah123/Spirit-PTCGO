"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_exeggcute_93_call_for_family,
)

card = PokemonCardDef(guid='59b50414-7655-5f4f-93e1-76de3f24a0f3', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name', display_name='Exeggcute', searchable_by=['Exeggcute', 'Basic', 'Exeggcute'], subtypes=['Basic'], collector_number=93, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=102, abilities=[Attack(title='Call for Family', game_text='Search your deck for up to 2 in any combination of Grass Basic Pokémon and Psychic Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp6_exeggcute_93_call_for_family()), Attack(title='Hypnosis', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.PSYCHIC: 1}, damage=10, effect=condition_attack(SpecialConditions.ASLEEP))])
