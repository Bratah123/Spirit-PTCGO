"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_darkrai_4_darkness_roar,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='48079458-1be0-5a29-8593-b2d809cd0c5e', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name', display_name='Darkrai', searchable_by=['Darkrai', 'Basic', 'Darkrai'], subtypes=['Basic'], collector_number=4, set_code='DP4', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=491, abilities=[Attack(title='Darkness Roar', game_text='You may have your opponent switch the Defending Pokémon with 1 or his or her Benched Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=dp4_darkrai_4_darkness_roar()), Attack(title='Sleep Hole', game_text='If the Defending Pokémon is Asleep, this attack does 40 damage plus 40 more damage. If the Defending Pokémon is not Asleep, that Pokémon is now Asleep.', cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=condition_attack(SpecialConditions.ASLEEP))])
