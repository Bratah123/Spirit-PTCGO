"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_golem_29_double_throw,
    dp3_golem_29_megaton_rock,
)

card = PokemonCardDef(guid='d5f77842-a53c-5aaa-829c-8179057808ec', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name', display_name='Golem', searchable_by=['Golem', 'Stage 2', 'Golem'], subtypes=['Stage 2'], collector_number=29, set_code='DP3', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name', family_id=76, abilities=[Attack(title='Double Throw', game_text="Choose 2 of your opponent's Pokémon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, effect=dp3_golem_29_double_throw()), Attack(title='Megaton Rock', game_text="You may do 40 damage instead of 80 to the Defending Pokémon. If you do, during your opponent's next turn, any damage done to Golem by attacks is reduced by 40 (after applying Weakness and Resistance).", cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1}, damage=80, effect=dp3_golem_29_megaton_rock())])
