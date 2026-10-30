"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_sceptile_8_leaf_blade,
    dp4_sceptile_8_wild_growth,
)

card = PokemonCardDef(guid='ce7ebef5-d739-5ff6-93df-219372a58072', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name', display_name='Sceptile', searchable_by=['Sceptile', 'Stage 2', 'Sceptile'], subtypes=['Stage 2'], collector_number=8, set_code='DP4', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name', family_id=252, abilities=[Ability(title='Wild Growth', game_text="Each basic Grass Energy card attached to your Grass Pokémon provides GrassGrass Energy instead. You can't use more than 1 Wild Growth Poké-Body each turn.", ability_type=AbilityTypes.POKE_BODY, effect=dp4_sceptile_8_wild_growth(), activation=Activations.ONCE_PER_TURN), Attack(title='Leaf Blade', game_text='Flip a coin. If heads, this attack does 50 damage plus 20 more damage.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=dp4_sceptile_8_leaf_blade())])
