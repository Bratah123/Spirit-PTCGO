"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_ludicolo_13_rain_dish,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='741aa55f-9d29-53f6-8cea-70afe2da640e', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name', display_name='Ludicolo', searchable_by=['Ludicolo', 'Stage 2', 'Ludicolo'], subtypes=['Stage 2'], collector_number=13, set_code='DP3', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name', family_id=270, abilities=[Ability(title='Rain Dish', game_text='At any time between turns, remove 1 damage counter from Ludicolo.', ability_type=AbilityTypes.POKE_BODY, effect=dp3_ludicolo_13_rain_dish(), activation=Activations.ONCE_PER_TURN), Attack(title='Nature Power', game_text='If you have a Stadium Card in play, this attack does 60 damage plus 20 more damage. If your opponent has a Stadium card in play, the Defending Pokémon is now Confused.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=60, damage_operator='+', effect=condition_attack(SpecialConditions.CONFUSED))])
