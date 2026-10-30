"""STUB: effect not implemented — do not guess mechanics.
Gastly (DP7 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_gastly_62_pitch_dark,
    switch_self_attack,
)

card = PokemonCardDef(guid='4c312e40-7050-5443-8231-8730b91694bf', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name', display_name='Gastly', searchable_by=['Gastly', 'Basic', 'Gastly'], subtypes=['Basic'], collector_number=62, set_code='DP7', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=92, abilities=[Attack(title='Pitch-Dark', game_text="You opponent can't play any Trainer cards from his or her hand during your opponent's next turn.", cost={}, effect=dp7_gastly_62_pitch_dark()), Attack(title='Trick Gas', game_text='You may switch Gastly with 1 of your Benched Pokémon.', cost={PokemonTypes.PSYCHIC: 1}, damage=10, effect=switch_self_attack(damage=10, optional=True))])
