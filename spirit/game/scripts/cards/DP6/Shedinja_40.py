"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_shedinja_40_curse_and_deceive,
    dp6_shedinja_40_resent,
)

card = PokemonCardDef(guid='565cd8ae-2bf3-5e1a-b184-3127b3b3fe3d', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name', display_name='Shedinja', searchable_by=['Shedinja', 'Stage 1', 'Shedinja'], subtypes=['Stage 1'], collector_number=40, set_code='DP6', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=0, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name', family_id=290, abilities=[Ability(title='Resent', game_text="Once during your opponent's turn, if Shedinja would be Knocked Out by damage from an attack, you may put 4 damage counters on the Attacking Pokémon and each of the opponent's Pokémon that has the same name as the Attacking Pokémon.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_shedinja_40_resent(), activation=Activations.ONCE_PER_TURN), Attack(title='Curse and Deceive', game_text='Put 3 damage counters on the Defending Pokémon. If Shedinja has any damage counters on it, the Defending Pokémon is now Confused.', cost={PokemonTypes.COLORLESS: 1}, effect=dp6_shedinja_40_curse_and_deceive())])
