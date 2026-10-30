"""STUB: effect not implemented — do not guess mechanics.
Scizor (DP7 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_scizor_25_accelerate,
    dp7_scizor_25_honeycomb_defender,
    dp7_scizor_25_pound_down,
)

card = PokemonCardDef(guid='ccca89b1-323a-5735-8273-9857ad47bc76', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name', display_name='Scizor', searchable_by=['Scizor', 'Stage 1', 'Scizor'], subtypes=['Stage 1'], collector_number=25, set_code='DP7', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name', family_id=123, abilities=[Ability(title='Honeycomb Defender', game_text='If Scizor has 6 or more damage counters on it, any damage done to Scizor by attacks is reduced by 40 (after applying Weakness and Resistance).', ability_type=AbilityTypes.POKE_BODY, effect=dp7_scizor_25_honeycomb_defender(), activation=Activations.ONCE_PER_TURN), Attack(title='Accelerate', game_text="If the Defending Pokémon is Knocked Out by this attack, prevent all effects of an attack, including damage, done to Scizor during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=dp7_scizor_25_accelerate()), Attack(title='Pound Down', game_text="If you don't have any Pokémon with any Poké-Powers in play, this attack does 40 damage plus 30 more damage.", cost={PokemonTypes.GRASS: 2}, damage=40, damage_operator='+', effect=dp7_scizor_25_pound_down())])
