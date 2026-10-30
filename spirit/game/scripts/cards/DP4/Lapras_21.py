"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_lapras_21_carry_in,
)

card = PokemonCardDef(guid='99c89bb4-edab-5b64-84e9-36482db9d79f', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name', display_name='Lapras', searchable_by=['Lapras', 'Basic', 'Lapras'], subtypes=['Basic'], collector_number=21, set_code='DP4', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=131, abilities=[Attack(title='Carry In', game_text='Search your deck for a Pokémon Tool Card, a Supporter card, and a basic Energy card, show them to your opponent, and put them into your hand. Shuffle your deck afterward.', cost={PokemonTypes.WATER: 1}, effect=dp4_lapras_21_carry_in()), Attack(title='Wave Splash', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=20)])
