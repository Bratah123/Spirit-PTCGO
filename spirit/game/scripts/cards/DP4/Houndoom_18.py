"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import knock_off_random_hand
from spirit.game.card_effects.dp import (
    dp4_houndoom_18_black_fire,
)

card = PokemonCardDef(guid='5f66d68b-775a-5410-826b-8fc06d387cd1', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name', display_name='Houndoom', searchable_by=['Houndoom', 'Stage 1', 'Houndoom'], subtypes=['Stage 1'], collector_number=18, set_code='DP4', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name', family_id=228, abilities=[Attack(title='Dark Fang', game_text="Choose 1 card from your opponent's hand without looking and discard it.", cost={PokemonTypes.DARKNESS: 1}, damage=20, effect=knock_off_random_hand()), Attack(title='Black Fire', game_text='You may discard a Fire or Darkness Energy attached to Houndoom. If you discard a Fire Energy, the Defending Pokémon is now Burned. If you discard a Darkness Energy, this attack does 40 damage plus 30 more damage.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=dp4_houndoom_18_black_fire())])
