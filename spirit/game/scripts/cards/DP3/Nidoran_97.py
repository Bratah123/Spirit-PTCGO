"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.dp import (
    dp3_nidoran_97_poison_skin,
)

card = PokemonCardDef(guid='b55da96a-990b-5f49-82cb-627acc0b6db1', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name', display_name='Nidoran ♂', searchable_by=['Nidoran ♂', 'Basic', 'Nidoran'], subtypes=['Basic'], collector_number=97, set_code='DP3', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=32, abilities=[Attack(title='Collect', game_text='Draw a card.', cost={PokemonTypes.COLORLESS: 1}, effect=draw_attack(1)), Attack(title='Poison Skin', game_text='Flip 2 coins. If either of them is heads, the Defending Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 1}, effect=dp3_nidoran_97_poison_skin())])
