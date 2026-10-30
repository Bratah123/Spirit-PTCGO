"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import silver_wind
from spirit.game.card_effects.dp import (
    dp6_armaldo_18_fossil_armor,
)

card = PokemonCardDef(guid='7550a1f7-0f5f-5fbc-8ad5-7184b47109c5', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name', display_name='Armaldo', searchable_by=['Armaldo', 'Stage 2', 'Armaldo'], subtypes=['Stage 2'], collector_number=18, set_code='DP6', rarity=Rarities.Rare, hp=140, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name', family_id=347, abilities=[Ability(title='Fossil Armor', game_text="If Armaldo would be damaged by an attack, prevent that attack's damage done to Armaldo if that damage is 60 or less.", ability_type=AbilityTypes.POKE_BODY, effect=dp6_armaldo_18_fossil_armor(), activation=Activations.ONCE_PER_TURN), Attack(title='Crush Claw', game_text='During your next turn, if an attack does damage to the Defending Pokémon (after applying Weakness and Resistance), that attack does 40 more damage.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=silver_wind(40))])
