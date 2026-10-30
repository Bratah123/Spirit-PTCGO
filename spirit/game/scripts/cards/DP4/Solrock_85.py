"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_solrock_85_sol_charge,
    dp4_solrock_85_sunlight,
)

card = PokemonCardDef(guid='9e5918e2-116d-51c8-8796-1b305c3887c2', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name', display_name='Solrock', searchable_by=['Solrock', 'Basic', 'Solrock'], subtypes=['Basic'], collector_number=85, set_code='DP4', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=338, abilities=[Ability(title='Sunlight', game_text="If you have Lunatone in play, damage done to your opponent's Pokémon by your Psychic or Fighting Pokémon isn't affected by resistance.", ability_type=AbilityTypes.POKE_BODY, effect=dp4_solrock_85_sunlight(), activation=Activations.ONCE_PER_TURN), Attack(title='Sol Charge', game_text='Search your discard pile for a basic Energy card and attach it to 1 of your Benched Pokémon.', cost={PokemonTypes.FIGHTING: 1}, damage=20, effect=dp4_solrock_85_sol_charge())])
