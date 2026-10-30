"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_shelgon_64_focus_energy,
    dp3_shelgon_64_protect_charge,
)

card = PokemonCardDef(guid='4d1d0090-22a3-5fcc-914a-e9fad69f64f7', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name', display_name='Shelgon', searchable_by=['Shelgon', 'Stage 1', 'Shelgon'], subtypes=['Stage 1'], collector_number=64, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name', family_id=371, abilities=[Attack(title='Focus Energy', game_text="During your next turn, Shelgon's Protect Charge attack's base damage is 80.", cost={PokemonTypes.COLORLESS: 1}, effect=dp3_shelgon_64_focus_energy()), Attack(title='Protect Charge', game_text="During your opponent's next turn, any damage done to Shelgon by attacks is reduced by 30 (after applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 3}, damage=30, effect=dp3_shelgon_64_protect_charge())])
