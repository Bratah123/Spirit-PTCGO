"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_cloyster_47_spine_missile,
    scrunch_protect,
)

card = PokemonCardDef(guid='a98f9f57-994c-5892-9ca5-39eaa5651fba', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name', display_name='Cloyster', searchable_by=['Cloyster', 'Stage 1', 'Cloyster'], subtypes=['Stage 1'], collector_number=47, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name', family_id=90, abilities=[Attack(title='Withdraw', game_text="Flip a coin. If heads, prevent all damage done to Cloyster by attacks during your opponent's next turn.", cost={}, effect=scrunch_protect()), Attack(title='Spine Missile', game_text="Flip 4 coins. For each heads, choose an opponent's Pokémon in play and this attack does 20 damage to those Pokémon. (You may choose the same Pokémon more than once.) (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, effect=dp3_cloyster_47_spine_missile())])
