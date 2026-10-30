"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp5_pachirisu_43_trans_tail,
)

card = PokemonCardDef(guid='e5572803-dab8-55ce-9e18-f05cd290e34d', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name', display_name='Pachirisu', searchable_by=['Pachirisu', 'Basic', 'Pachirisu'], subtypes=['Basic'], collector_number=43, set_code='DP5', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=417, abilities=[Attack(title='Trans Tail', game_text='Search your discard pile for a Lightning Energy card, show it to your opponent, and put it into your hand.', cost={}, effect=dp5_pachirisu_43_trans_tail()), Attack(title='Thundershock', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
