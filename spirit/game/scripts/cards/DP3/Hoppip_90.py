"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_hoppip_90_cottonweed,
    dp3_hoppip_90_hover_heal,
)

card = PokemonCardDef(guid='40065178-693f-5bda-b393-4024d6c8974a', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name', display_name='Hoppip', searchable_by=['Hoppip', 'Basic', 'Hoppip'], subtypes=['Basic'], collector_number=90, set_code='DP3', rarity=Rarities.Common, hp=30, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=187, abilities=[Ability(title='Cottonweed', game_text='If Hoppip has any Grass Energy attached to it, the Retreat Cost for Hoppip is 0.', ability_type=AbilityTypes.POKE_BODY, effect=dp3_hoppip_90_cottonweed(), activation=Activations.ONCE_PER_TURN), Attack(title='Hover Heal', game_text='Remove all Special Conditions from Hoppip.', cost={PokemonTypes.GRASS: 1}, damage=10, effect=dp3_hoppip_90_hover_heal())])
