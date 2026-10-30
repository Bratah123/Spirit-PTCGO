"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_porygon2_49_download,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='6a0b3469-709f-5819-a499-c9b0a51f596e', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name', display_name='Porygon2', searchable_by=['Porygon2', 'Stage 1', 'Porygon2'], subtypes=['Stage 1'], collector_number=49, set_code='DP4', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name', family_id=137, abilities=[Ability(title='Download', game_text="Once during your turn (before your attack), you may discard a Supporter card from your hand and use the effect of that card as the effect of this power. This power can't be used if Porygon2 is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_porygon2_49_download(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Speed Attack', cost={PokemonTypes.COLORLESS: 2}, damage=30)])
