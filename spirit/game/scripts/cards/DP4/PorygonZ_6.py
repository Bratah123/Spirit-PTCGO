"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_porygonz_6_conversion,
    multi_flip_damage,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='b00112f2-ca6e-5b16-9957-fa4fa76d14c9', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name', display_name='Porygon-Z', searchable_by=['Porygon-Z', 'Stage 2', 'PorygonZ'], subtypes=['Stage 2'], collector_number=6, set_code='DP4', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name', family_id=137, abilities=[Ability(title='Conversion', game_text="Once during your turn (before your attack), you may discard a basic Energy card from your hand. Porygon-Z is the same type as that Energy Card until the end of your turn. This power can't be used if Porygon-Z is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_porygonz_6_conversion(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Tri Attack', game_text='Flip 3 coins. This attack does 40 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='x', effect=multi_flip_damage(3, 40))])
