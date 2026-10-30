"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_sneasel_120_rob,
)

card = PokemonCardDef(guid='86e54be5-e3e3-5852-b6da-deb359bff2ee', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name', display_name='Sneasel', searchable_by=['Sneasel', 'Basic', 'Sneasel'], subtypes=['Basic'], collector_number=120, set_code='DP6', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=215, abilities=[Attack(title='Rob', game_text="Look at your opponent's hand. If your opponent has any Pokémon Tool or Technical Machine cards in his or her hand, put those cards on top of his or her deck. Your opponent shuffles his or her deck afterward.", cost={PokemonTypes.DARKNESS: 1}, effect=dp6_sneasel_120_rob()), Attack(title='Slash', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
