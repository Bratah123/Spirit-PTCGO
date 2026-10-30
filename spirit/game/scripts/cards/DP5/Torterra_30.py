"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_torterra_30_earthquake,
    dp5_torterra_30_frenzy_plant,
)

card = PokemonCardDef(guid='48bccc44-51c0-5f0e-9ce6-eaa8e8d6ba09', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name', display_name='Torterra', searchable_by=['Torterra', 'Stage 2', 'Torterra'], subtypes=['Stage 2'], collector_number=30, set_code='DP5', rarity=Rarities.Rare, hp=140, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name', family_id=387, abilities=[Attack(title='Earthquake', game_text="Does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 2}, damage=60, effect=dp5_torterra_30_earthquake()), Attack(title='Frenzy Plant', game_text="Torterra can't use Frenzy Plant during your next turn.", cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2}, damage=100, effect=dp5_torterra_30_frenzy_plant())])
