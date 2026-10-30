"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_mewtwolvx_144_giga_burn,
    dp6_mewtwolvx_144_psybarrier,
)

card = PokemonCardDef(guid='1bf65806-1eef-5a40-9298-a5342ac062b4', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoLVX.Name', display_name='Mewtwo LV.X', searchable_by=['Mewtwo LV.X', 'Level-Up', 'MewtwoLVX'], subtypes=['Level-Up'], collector_number=144, set_code='DP6', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.LEVELUP, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name', family_id=150, abilities=[Ability(title='Psybarrier', game_text="Prevent all effects of attacks, including damage, done to Mewtwo by your opponent's Pokémon that isn't an Evolved Pokémon.", ability_type=AbilityTypes.POKE_BODY, effect=dp6_mewtwolvx_144_psybarrier(), activation=Activations.ONCE_PER_TURN), Attack(title='Giga Burn', game_text='Discard all Energy attached to Mewtwo.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=120, effect=dp6_mewtwolvx_144_giga_burn())])
