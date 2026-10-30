"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_darkrailvx_104_dark_shadow,
    dp4_darkrailvx_104_endless_darkness,
)

card = PokemonCardDef(guid='c09437d8-2f59-50ff-a34a-7329c1d90131', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiLVX.Name', display_name='Darkrai LV.X', searchable_by=['Darkrai LV.X', 'Level-Up', 'DarkraiLVX'], subtypes=['Level-Up'], collector_number=104, set_code='DP4', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.LEVELUP, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name', family_id=491, abilities=[Ability(title='Dark Shadow', game_text='Each basic Darkness Energy card attached to your Darkness Pokémon now has the effect "If the Pokémon Darkness Energy is attached to attacks, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance)." You can\'t use more than 1 Dark Shadow Poké-Body each turn.', ability_type=AbilityTypes.POKE_BODY, effect=dp4_darkrailvx_104_dark_shadow(), activation=Activations.ONCE_PER_TURN), Attack(title='Endless Darkness', game_text='The Defending Pokémon is now Asleep. Flip 2 coins instead of 1 between turns. If either of them is tails, the Defending Pokémon is still Asleep. If both of them are tails, the Defending Pokémon is Knocked Out.', cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp4_darkrailvx_104_endless_darkness())])
