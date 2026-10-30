"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_skiploom_65_cotton_balloon,
    dp3_skiploom_65_u_turn,
)

card = PokemonCardDef(guid='81a57251-9148-5989-827d-cb50b9b91a91', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name', display_name='Skiploom', searchable_by=['Skiploom', 'Stage 1', 'Skiploom'], subtypes=['Stage 1'], collector_number=65, set_code='DP3', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name', family_id=187, abilities=[Ability(title='Cotton Balloon', game_text="If Skiploom has any Grass Energy attached to it, any damage done to Skiploom by attacks from your opponent's Evolved Pokémon is reduced by 20 (after applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=dp3_skiploom_65_cotton_balloon(), activation=Activations.ONCE_PER_TURN), Attack(title='U-turn', game_text='Switch Skiploom with 1 of your Benched Pokémon.', cost={PokemonTypes.GRASS: 1}, damage=20, effect=dp3_skiploom_65_u_turn())])
