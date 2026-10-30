"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_ampharos_1_cluster_bolt,
    dp3_ampharos_1_jamming_passive,
)

card = PokemonCardDef(guid='256da3ec-839d-566d-b6ad-bbd822345b22', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name', display_name='Ampharos', searchable_by=['Ampharos', 'Stage 2', 'Ampharos'], subtypes=['Stage 2'], collector_number=1, set_code='DP3', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name', family_id=179, abilities=[Ability(title='Jamming', game_text="After your opponent plays a Supporter card from his or her hand, put 1 damage counter on each of your opponent's Pokémon. You can't use more than 1 Jamming Poké-Body each turn.", ability_type=AbilityTypes.POKE_BODY, passive=dp3_ampharos_1_jamming_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Cluster Bolt', game_text="You may discard all Lightning Energy attached to Ampharos. If you do, this attack does 20 damage to each of your opponent's Benched Pokémon that has any Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=70, effect=dp3_ampharos_1_cluster_bolt())])
