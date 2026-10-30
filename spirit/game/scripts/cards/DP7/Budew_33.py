"""STUB: effect not implemented — do not guess mechanics.
Budew (DP7 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.dp import (
    dp7_budew_33_buddy_buddy,
    dp7_budew_33_poison_enzyme,
)

card = PokemonCardDef(guid='8148d161-27a5-5fad-b5c1-181d59e77a39', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Budew.Name', display_name='Budew', searchable_by=['Budew', 'Basic', 'Budew'], subtypes=['Basic'], collector_number=33, set_code='DP7', rarity=Rarities.Uncommon, hp=40, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=406, abilities=[Ability(title='Poison Enzyme', game_text="Prevent all effects of attacks, including damage, done to Budew by your opponent's Poisoned Pokémon.", ability_type=AbilityTypes.POKE_BODY, effect=dp7_budew_33_poison_enzyme(), activation=Activations.ONCE_PER_TURN), Ability(title='Baby Evolution', game_text='Once during your turn (before your attack), you may put Roselia from your hand onto Budew (this counts as evolving Budew) and remove all damage counters from Budew.', ability_type=AbilityTypes.POKE_POWER, condition=baby_evolution_condition('Roselia'), effect=baby_evolution('Roselia')), Attack(title='Buddy-buddy', game_text='Search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={}, effect=dp7_budew_33_buddy_buddy())])
