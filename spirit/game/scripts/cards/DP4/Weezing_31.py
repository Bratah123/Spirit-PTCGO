"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_weezing_31_toxic_virus_passive,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='db024c8e-864f-5668-8d02-cb2f1306a512', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name', display_name='Weezing', searchable_by=['Weezing', 'Stage 1', 'Weezing'], subtypes=['Stage 1'], collector_number=31, set_code='DP4', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name', family_id=109, abilities=[Ability(title='Toxic Virus', game_text='At any time between turns, each player puts 1 more damage counter on his or her Poisoned Pokémon.', ability_type=AbilityTypes.POKE_BODY, passive=dp4_weezing_31_toxic_virus_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Offensive Gas', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused and Poisoned.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.CONFUSED, flip=True))])
