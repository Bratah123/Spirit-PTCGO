"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_kabutops_6_chop_up,
    dp5_kabutops_6_primal_shell_passive,
)

card = PokemonCardDef(guid='82fdd3ad-bae0-50f6-a32f-ea29cf36126b', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name', display_name='Kabutops', searchable_by=['Kabutops', 'Stage 2', 'Kabutops'], subtypes=['Stage 2'], collector_number=6, set_code='DP5', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name', family_id=140, abilities=[Ability(title='Primal Shell', game_text="As long as Kabutops is your Active Pokémon, your opponent can't play any Trainer cards from his or her hand.", ability_type=AbilityTypes.POKE_BODY, passive=dp5_kabutops_6_primal_shell_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Chop Up', game_text="Does 10 damage to each of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=70, effect=dp5_kabutops_6_chop_up())])
