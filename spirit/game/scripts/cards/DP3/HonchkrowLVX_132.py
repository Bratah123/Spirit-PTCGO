"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_honchkrowlvx_132_darkness_wing,
    dp3_honchkrowlvx_132_feint_attack,
)

card = PokemonCardDef(guid='4508bfe7-4237-54d1-a985-bb9bed547048', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.HonchkrowLVX.Name', display_name='Honchkrow LV.X', searchable_by=['Honchkrow LV.X', 'Level-Up', 'HonchkrowLVX'], subtypes=['Level-Up'], collector_number=132, set_code='DP3', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.LEVELUP, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name', family_id=430, abilities=[Attack(title='Feint Attack', game_text="Choose 1 of your opponent's Pokémon. This attack does 40 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.COLORLESS: 2}, effect=dp3_honchkrowlvx_132_feint_attack()), Attack(title='Darkness Wing', game_text='If the Defending Pokémon would be Knocked Out by damage from this attack, you may search your discard pile for any 1 card, show it to your opponent, and put it into your hand.', cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp3_honchkrowlvx_132_darkness_wing())])
