"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import dp4_solrock_85_sol_charge
from spirit.game.card_effects.dp import (
    dp6_delcatty_23_attracting_body,
)

card = PokemonCardDef(guid='23149dd4-dfb6-5796-8814-a77de41d2b3e', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name', display_name='Delcatty', searchable_by=['Delcatty', 'Stage 1', 'Delcatty'], subtypes=['Stage 1'], collector_number=23, set_code='DP6', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name', family_id=300, abilities=[Ability(title='Attracting Body', game_text="If Delcatty is your Active Pokémon and is damaged by an opponent's attack (even if Delcatty is Knocked Out), flip a coin. If heads, the Attacking Pokémon is now Confused.", ability_type=AbilityTypes.POKE_BODY, effect=dp6_delcatty_23_attracting_body(), activation=Activations.ONCE_PER_TURN), Attack(title='Energy Assist', game_text='Search your discard pile for a basic Energy card and attach it to 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=30, effect=dp4_solrock_85_sol_charge())])
