"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_seviper_52_poison_tail,
    dp4_seviper_52_tail_blade,
)

card = PokemonCardDef(guid='879c07ae-e389-5a0f-a41a-a2f4554b12ff', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name', display_name='Seviper', searchable_by=['Seviper', 'Basic', 'Seviper'], subtypes=['Basic'], collector_number=52, set_code='DP4', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=336, abilities=[Attack(title='Tail Blade', game_text="Flip a coin. If heads, your opponent can't play any Trainer cards from his or her hand during your opponent's next turn.", cost={PokemonTypes.PSYCHIC: 1}, damage=20, effect=dp4_seviper_52_tail_blade()), Attack(title='Poison Tail', game_text='Flip a coin. If heads, this attack does 30 damage plus 30 more damage and the Defending Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=dp4_seviper_52_poison_tail())])
