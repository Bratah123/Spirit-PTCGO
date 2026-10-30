"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_mawile_24_jaw_bite,
    dp4_mawile_24_pick_out,
)

card = PokemonCardDef(guid='234339b0-47c7-5260-b759-f7c16efc1289', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name', display_name='Mawile', searchable_by=['Mawile', 'Basic', 'Mawile'], subtypes=['Basic'], collector_number=24, set_code='DP4', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=303, abilities=[Attack(title='Pick Out', game_text="Choose 1 face-down Prize card (yours or your opponent's) and put it face up. If that card is a Supporter card, use the effect of that card as the effect of this attack. (That card remains face up for the rest of the game.)", cost={}, effect=dp4_mawile_24_pick_out()), Attack(title='Jaw Bite', game_text='During your next turn, if an attack does damage to the Defending Pokémon (after applying Weakness and Resistance), that attack does 20 more damage.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=dp4_mawile_24_jaw_bite())])
