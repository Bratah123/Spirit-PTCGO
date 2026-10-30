"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_rotom_7_astonish,
    dp4_rotom_7_telebeam,
)

card = PokemonCardDef(guid='fd201df9-47d6-5508-b2a2-04c53cb8f566', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name', display_name='Rotom', searchable_by=['Rotom', 'Basic', 'Rotom'], subtypes=['Basic'], collector_number=7, set_code='DP4', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=479, abilities=[Attack(title='Astonish', game_text="Choose 1 card from your opponent's hand without looking. Look at that card you chose, then have your opponent shuffle that card into his or her deck.", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=dp4_rotom_7_astonish()), Attack(title='Telebeam', game_text='Flip a coin. If heads, this attack does 30 damage plus 30 more damage and the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.LIGHTNING: 2}, damage=30, damage_operator='+', effect=dp4_rotom_7_telebeam())])
