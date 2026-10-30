"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_bronzong_16_coating,
    dp5_bronzong_16_cursed_alloy_passive,
    dp5_bronzong_16_pain_amplifier,
)

card = PokemonCardDef(guid='e17e9aa5-0b4f-5172-8c2d-b29287d22668', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name', display_name='Bronzong', searchable_by=['Bronzong', 'Stage 1', 'Bronzong'], subtypes=['Stage 1'], collector_number=16, set_code='DP5', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.FIRE, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name', family_id=436, abilities=[Ability(title='Cursed Alloy', game_text="As long as Bronzong is your Active Pokémon, put 1 damage counter on each of your opponent's Pokémon that has any Poké-Powers between turns.", ability_type=AbilityTypes.POKE_BODY, passive=dp5_bronzong_16_cursed_alloy_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Pain Amplifier', game_text="Put 1 damage counter on each of your opponent's Pokémon that already has damage counters on it.", cost={}, effect=dp5_bronzong_16_pain_amplifier()), Attack(title='Coating', game_text="During your opponent's next turn, any damage done to Bronzong by attacks is reduced by 20 (after applying Weakness and Resistance).", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp5_bronzong_16_coating())])
