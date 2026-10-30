"""STUB: effect not implemented — do not guess mechanics.
Bibarel (DP7 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import amnesia
from spirit.game.card_effects.dp import (
    dp7_bibarel_32_unaware,
)

card = PokemonCardDef(guid='d2c41fdb-28ca-526c-ae26-ee2f7c27d019', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name', display_name='Bibarel', searchable_by=['Bibarel', 'Stage 1', 'Bibarel'], subtypes=['Stage 1'], collector_number=32, set_code='DP7', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name', family_id=399, abilities=[Ability(title='Unaware', game_text='Prevent all effects of attacks, excluding damage, done to Bibarel.', ability_type=AbilityTypes.POKE_BODY, effect=dp7_bibarel_32_unaware(), activation=Activations.ONCE_PER_TURN), Attack(title='Amnesia', game_text="Choose 1 of the Defending Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=amnesia), Attack(title='Surf', cost={PokemonTypes.WATER: 2}, damage=60)])
