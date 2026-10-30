"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_togekiss_11_air_scroll,
    dp4_togekiss_11_serene_grace,
)

card = PokemonCardDef(guid='13952052-7b5c-57fe-a45a-a66bb0715b64', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name', display_name='Togekiss', searchable_by=['Togekiss', 'Stage 2', 'Togekiss'], subtypes=['Stage 2'], collector_number=11, set_code='DP4', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name', family_id=175, abilities=[Ability(title='Serene Grace', game_text='Once during your turn, when you play Togekiss from your hand to evolve 1 of your Pokémon, you may look at the top 10 cards of your deck, choose as many basic Energy cards as you like, and attach them to your Pokémon in any way you like. Put the other cards back on top of your deck. Shuffle your deck afterward.', ability_type=AbilityTypes.POKE_POWER, effect=dp4_togekiss_11_serene_grace(), activation=Activations.ONCE_PER_TURN), Attack(title='Air Scroll', game_text='Flip a coin. If heads, this attack does 40 damage plus 30 more damage. If tails, remove 3 damage counters from Togekiss.', cost={PokemonTypes.COLORLESS: 3}, damage=40, damage_operator='+', effect=dp4_togekiss_11_air_scroll())])
