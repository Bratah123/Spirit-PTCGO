"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.dp import (
    dp5_palkia_11_pearl_blast,
)

card = PokemonCardDef(guid='775cba0f-4bb0-5fc6-8368-ea6f3becc65f', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name', display_name='Palkia', searchable_by=['Palkia', 'Basic', 'Palkia'], subtypes=['Basic'], collector_number=11, set_code='DP5', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, family_id=484, abilities=[Attack(title='Zone Shift', game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.', cost={PokemonTypes.WATER: 1}, effect=gust_attack(opponent_chooses=True)), Attack(title='Pearl Blast', game_text="You may return an Energy card attached to Palkia to your hand. If you do, choose an Energy card attached to the Defending Pokémon and return it to your opponent's hand.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp5_palkia_11_pearl_blast())])
