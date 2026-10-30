"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_milotic_25_marvel_scale_passive,
    dp4_milotic_25_twister,
)

card = PokemonCardDef(guid='8493990b-978d-5179-a760-b5fc2bf5408f', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name', display_name='Milotic', searchable_by=['Milotic', 'Stage 1', 'Milotic'], subtypes=['Stage 1'], collector_number=25, set_code='DP4', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name', family_id=349, abilities=[Ability(title='Marvel Scale', game_text="Prevent all effects of attacks, including damage, done to Milotic by your opponent's Pokémon LV.X.", ability_type=AbilityTypes.POKE_BODY, passive=dp4_milotic_25_marvel_scale_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Twister', game_text='Flip 2 coins. If both are tails, this attack does nothing. For each heads, discard an Energy attached to the Defending Pokémon.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=dp4_milotic_25_twister())])
