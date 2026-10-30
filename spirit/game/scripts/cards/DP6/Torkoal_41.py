"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp6_torkoal_41_white_smoke_passive,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='69a72791-aa18-5a69-a863-b141d3dd539d', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name', display_name='Torkoal', searchable_by=['Torkoal', 'Basic', 'Torkoal'], subtypes=['Basic'], collector_number=41, set_code='DP6', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.WATER, family_id=324, abilities=[Ability(title='White Smoke', game_text="As long as Torkoal is your Active Pokémon, prevent all effects, including damage, done to your Benched Pokémon by your opponent's attacks.", ability_type=AbilityTypes.POKE_BODY, passive=dp6_torkoal_41_white_smoke_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Black Soot', game_text='Flip a coin. If heads, the Defending Pokémon is now Burned and Paralyzed.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.BURNED, flip=True))])
