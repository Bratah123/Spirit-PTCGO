"""STUB: effect not implemented — do not guess mechanics.
Combee (DP7 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_combee_57_alert,
)

card = PokemonCardDef(guid='41b5abce-a346-5044-a7c2-b691e1d5da87', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name', display_name='Combee', searchable_by=['Combee', 'Basic', 'Combee'], subtypes=['Basic'], collector_number=57, set_code='DP7', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=415, abilities=[Attack(title='Alert', game_text='Draw a card. Then, you may switch Combee with 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 1}, effect=dp7_combee_57_alert())])
