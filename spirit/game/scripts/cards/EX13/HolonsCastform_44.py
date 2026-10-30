"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    delta_draw_up_to,
)

card = PokemonCardDef(guid='37d114e0-b3c9-5452-93c4-09ba6aae18f6', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.HolonsCastform.Name', display_name="Holon's Castform", searchable_by=["Holon's Castform", 'Basic', 'HolonsCastform'], subtypes=['Basic'], collector_number=44, set_code='EX13', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=351, abilities=[Attack(title='Delta Draw', game_text='Count the number of Pokémon you have in play that has δ on its card. Draw up to that many cards.', cost={PokemonTypes.COLORLESS: 1}, effect=delta_draw_up_to())])
