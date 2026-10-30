"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_mewtwo_11_psychic,
)

card = PokemonCardDef(guid='2187f3f2-e26e-5871-8109-adea956275e8', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name', display_name='Mewtwo', searchable_by=['Mewtwo', 'Basic', 'Mewtwo'], subtypes=['Basic'], collector_number=11, set_code='DP6', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=150, abilities=[Attack(title='Hypnoblast', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Psychic', game_text='Does 40 damage plus 10 more damage for each Energy attached to the Defending Pokémon.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=dp6_mewtwo_11_psychic())])
