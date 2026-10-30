"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_mewtwo_9_energy_absorption,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(guid='56a8af55-0d7d-59c9-af4e-de73f453caf7', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name', display_name='Mewtwo', searchable_by=['Mewtwo', 'Basic', 'Mewtwo'], subtypes=['Basic'], collector_number=9, set_code='DP5', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=150, abilities=[Attack(title='Energy Absorption', game_text='Search your discard pile for up to 2 Energy cards and attach them to Mewtwo.', cost={}, effect=dp5_mewtwo_9_energy_absorption()), Attack(title='Recover', game_text='Discard a Psychic Energy attached to Mewtwo and remove 6 damage counters from Mewtwo.', cost={PokemonTypes.PSYCHIC: 1}, effect=self_energy_discard_attack(count=1, then_damage=0)), Attack(title='Psyburn', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=60)])
