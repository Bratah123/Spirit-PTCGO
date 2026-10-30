"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_charizard_3_blast_burn,
    dp3_charizard_3_fury_blaze,
)

card = PokemonCardDef(guid='efa3f6be-164c-5c6b-a20b-c630ec2a8471', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name', display_name='Charizard', searchable_by=['Charizard', 'Stage 2', 'Charizard'], subtypes=['Stage 2'], collector_number=3, set_code='DP3', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name', family_id=4, abilities=[Ability(title='Fury Blaze', game_text="If your opponent has 3 or less Prize cards left, each of Charizard's attacks does 50 more damage to the Active Pokémon (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=dp3_charizard_3_fury_blaze(), activation=Activations.ONCE_PER_TURN), Attack(title='Blast Burn', game_text="Flip a coin. If heads, discard 2 Energy cards attached to Charizard. If tails, discard 4 Energy cards attached to Charizard. (If you can't, this attack does nothing.)", cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1}, damage=120, effect=dp3_charizard_3_blast_burn())])
