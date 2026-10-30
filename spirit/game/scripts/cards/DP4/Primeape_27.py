"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_primeape_27_anger_point,
    dp4_primeape_27_whump,
)

card = PokemonCardDef(guid='6f45d1d3-319d-5605-bb0c-ed560e53629a', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name', display_name='Primeape', searchable_by=['Primeape', 'Stage 1', 'Primeape'], subtypes=['Stage 1'], collector_number=27, set_code='DP4', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name', family_id=56, abilities=[Ability(title='Anger Point', game_text="If Primeape has any damage counters on it, Primeape's attacks do 40 more damage to the Active Pokémon (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=dp4_primeape_27_anger_point(), activation=Activations.ONCE_PER_TURN), Attack(title='Whump', game_text="Primeape is now Confused. Flip a coin. If heads, the Defending Pokémon can't attack during your opponent's next turn.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=dp4_primeape_27_whump())])
