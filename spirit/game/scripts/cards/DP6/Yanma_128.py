"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    switch_self_attack,
)
from spirit.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(guid='c27d9507-10a7-5a34-8cd8-435756107516', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name', display_name='Yanma', searchable_by=['Yanma', 'Basic', 'Yanma'], subtypes=['Basic'], collector_number=128, set_code='DP6', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=193, abilities=[Attack(title='U-turn', game_text='Switch Yanma with 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=switch_self_attack(damage=10)), Attack(title='Agility', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Yanma during your opponent's next turn.", cost={PokemonTypes.GRASS: 2}, damage=20, effect=flip_protection(prevent=True, effects_too=True, title='Agility'))])
