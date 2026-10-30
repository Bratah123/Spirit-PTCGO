"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.dp import (
    switch_self_attack,
)

card = PokemonCardDef(guid='9e445160-00c8-559d-b89a-731c495e3f39', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name', display_name='Horsea', searchable_by=['Horsea', 'Basic', 'Horsea'], subtypes=['Basic'], collector_number=102, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=116, abilities=[Attack(title='Smokescreen', game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.", cost={PokemonTypes.COLORLESS: 1}, effect=smokescreen_attack()), Attack(title='Reverse Thrust', game_text='Switch Horsea with 1 of your Benched Pokémon.', cost={PokemonTypes.WATER: 1}, damage=10, effect=switch_self_attack(damage=10))])
