"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_sunflora_38_grass_whistle,
    multi_flip_damage,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='653756ce-94c6-5794-933a-86a83981d1d5', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name', display_name='Sunflora', searchable_by=['Sunflora', 'Stage 1', 'Sunflora'], subtypes=['Stage 1'], collector_number=38, set_code='DP3', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name', family_id=191, abilities=[Ability(title='Grass Whistle', game_text="Once during your turn (before your attack), you may remove 1 damage counter from each of your Grass Pokémon. You can't use more than 1 Grass Whistle Poké-Power each turn. This power can't be used if Sunflora is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_sunflora_38_grass_whistle(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Petal Dance', game_text='Flip 3 coins. This attack does 30 damage times the number of heads. If you get 2 or more heads, Sunflora is now Confused.', cost={PokemonTypes.GRASS: 2}, damage=30, damage_operator='x', effect=multi_flip_damage(3, 30))])
