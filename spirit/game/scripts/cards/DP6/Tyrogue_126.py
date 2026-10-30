"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_tyrogue_126_baby_evolution,
    dp6_tyrogue_126_gut_blow,
)

card = PokemonCardDef(guid='32470b60-ec5b-539e-b073-102b0b7b8d8a', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name', display_name='Tyrogue', searchable_by=['Tyrogue', 'Basic', 'Tyrogue'], subtypes=['Basic'], collector_number=126, set_code='DP6', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=236, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Hitmonlee, Hitmonchan, or Hitmontop from your hand onto Tyrogue (this counts as evolving Tyrogue) and remove all damage counters from Tyrogue.', ability_type=AbilityTypes.POKE_POWER, effect=dp6_tyrogue_126_baby_evolution(), activation=Activations.ONCE_PER_TURN), Attack(title='Gut Blow', game_text='If the Defending Pokémon is an Evolved Pokémon, this attack does 10 damage plus 20 more damage and Tyrogue does 10 damage to itself.', cost={PokemonTypes.FIGHTING: 1}, damage=10, damage_operator='+', effect=dp6_tyrogue_126_gut_blow())])
