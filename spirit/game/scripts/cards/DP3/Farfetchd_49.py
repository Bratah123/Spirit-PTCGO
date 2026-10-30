"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_farfetchd_49_leek_slap,
    dp3_farfetchd_49_swords_dance,
)

card = PokemonCardDef(guid='b39abbba-012e-53e0-81ff-e26f2ef93346', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name', display_name="Farfetch'd", searchable_by=["Farfetch'd", 'Basic', 'Farfetchd'], subtypes=['Basic'], collector_number=49, set_code='DP3', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=83, abilities=[Attack(title='Swords Dance', game_text="During your next turn, Farfetch'd's Leek Slap attack's base damage is 60.", cost={PokemonTypes.COLORLESS: 1}, effect=dp3_farfetchd_49_swords_dance()), Attack(title='Leek Slap', game_text="During your next turn, Farfetch'd can't use Leek Slap.", cost={PokemonTypes.COLORLESS: 1}, damage=30, effect=dp3_farfetchd_49_leek_slap())])
