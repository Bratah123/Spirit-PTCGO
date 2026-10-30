"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_lugia_14_psychic_destruction,
    dp3_lugia_14_silver_wing,
)

card = PokemonCardDef(guid='b2558fe8-1e49-5903-b01c-1ad81057f683', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name', display_name='Lugia', searchable_by=['Lugia', 'Basic', 'Lugia'], subtypes=['Basic'], collector_number=14, set_code='DP3', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=249, abilities=[Attack(title='Silver Wing', game_text="Flip a coin. If heads, choose an Energy card attached to the Defending Pokémon and return it to your opponent's hand.", cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=dp3_lugia_14_silver_wing()), Attack(title='Psychic Destruction', game_text="If the Defending Pokémon has any Energy cards attached to it, this attack's base damage is 40 instead of 120.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=120, effect=dp3_lugia_14_psychic_destruction())])
