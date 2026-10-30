"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import (
    dragonbreath_paralyze,
)

card = PokemonCardDef(guid='5f3135a7-537a-5936-914d-f48904f4d4cd', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name', display_name='Latios δ', searchable_by=['Latios δ', 'Basic', 'Latios'], subtypes=['Basic'], collector_number=22, set_code='EX13', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.GRASS, family_id=381, abilities=[Attack(title='Aqua Wave', game_text='Flip a coin. If heads, this attack does 10 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='+', effect=flip_bonus(20)), Attack(title='Dragonbreath', game_text='Flip a coin. If tails, this attack does nothing. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=dragonbreath_paralyze())])
