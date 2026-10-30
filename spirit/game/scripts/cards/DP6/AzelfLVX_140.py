"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_azelflvx_140_deep_balance,
    dp6_azelflvx_140_psychic_aura,
)

card = PokemonCardDef(guid='88a6d6d8-7d92-5426-90e5-7c254944257d', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.AzelfLVX.Name', display_name='Azelf LV.X', searchable_by=['Azelf LV.X', 'Level-Up', 'AzelfLVX'], subtypes=['Level-Up'], collector_number=140, set_code='DP6', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.LEVELUP, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name', family_id=482, abilities=[Ability(title='Psychic Aura', game_text='Each of your Psychic Pokémon has no Weakness.', ability_type=AbilityTypes.POKE_BODY, effect=dp6_azelflvx_140_psychic_aura(), activation=Activations.ONCE_PER_TURN), Attack(title='Deep Balance', game_text="Choose 1 of your opponent's Pokémon. Put 1 damage counter on that Pokémon for each Energy attached to all of your opponent's Pokémon.", cost={PokemonTypes.PSYCHIC: 1}, effect=dp6_azelflvx_140_deep_balance())])
