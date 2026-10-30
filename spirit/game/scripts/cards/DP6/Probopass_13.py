"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_probopass_13_metal_bomber,
    dp6_probopass_13_steel_coating,
)

card = PokemonCardDef(guid='2c575021-76ed-54fb-9d6d-ad56f3d5d0c2', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name', display_name='Probopass', searchable_by=['Probopass', 'Stage 1', 'Probopass'], subtypes=['Stage 1'], collector_number=13, set_code='DP6', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name', family_id=299, abilities=[Ability(title='Steel Coating', game_text="Any damage done to Probopass by your opponent's attacks is reduced by 10 for each Metal Energy attached to Probopass (after applying Weakness and Resistance). You can't reduce more than 20 damage in this way.", ability_type=AbilityTypes.POKE_BODY, effect=dp6_probopass_13_steel_coating(), activation=Activations.ONCE_PER_TURN), Attack(title='Metal Bomber', game_text="Choose a number of your opponent's Benched Pokémon up to the amount of Metal Energy attached to Probopass. This attack does 20 damage to each of them. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp6_probopass_13_metal_bomber())])
