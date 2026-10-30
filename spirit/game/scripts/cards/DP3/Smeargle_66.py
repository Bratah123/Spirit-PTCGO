"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_smeargle_66_color_pick,
    dp3_smeargle_66_trace,
)

card = PokemonCardDef(guid='c11ba8f4-1291-5e79-ab25-8660c16f9f95', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name', display_name='Smeargle', searchable_by=['Smeargle', 'Basic', 'Smeargle'], subtypes=['Basic'], collector_number=66, set_code='DP3', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=235, abilities=[Attack(title='Color Pick', game_text='Search your deck for up to 3 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.', cost={}, effect=dp3_smeargle_66_color_pick()), Attack(title='Trace', game_text="Flip a coin. If heads, choose an attack on 1 of your opponent's Benched Pokémon. Trace copies that attack except for its Energy cost. (You must still do anything else required for that attack.) Smeargle performs that attack.", cost={PokemonTypes.COLORLESS: 1}, effect=dp3_smeargle_66_trace())])
