"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    lively_heal_draw,
)
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition

card = PokemonCardDef(guid='f94c9882-8123-5796-b350-5ce5f432c969', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Happiny.Name', display_name='Happiny', searchable_by=['Happiny', 'Basic', 'Happiny'], subtypes=['Basic'], collector_number=52, set_code='DP2', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=440, abilities=[Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Chansey from your hand onto Happiny (this counts as evolving Happiny) and remove all damage counters from Happiny.', ability_type=AbilityTypes.POKE_POWER, effect=baby_evolution('Chansey'), activation=Activations.ONCE_PER_TURN, condition=baby_evolution_condition('Chansey')), Attack(title='Lively', game_text='Remove 2 damage counters from 1 of your Pokémon.', cost={}, effect=lively_heal_draw())])
