"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_weavile_40_chip_off,
    dp3_weavile_40_dark_engage,
    dp3_weavile_40_shadow_charge,
)

card = PokemonCardDef(guid='5fdb3555-bb4f-5945-934e-6b33e8cb4b14', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name', display_name='Weavile', searchable_by=['Weavile', 'Stage 1', 'Weavile'], subtypes=['Stage 1'], collector_number=40, set_code='DP3', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name', family_id=461, abilities=[Ability(title='Dark Engage', game_text="Once during your turn (before your attack), you may use this power. Each of your Active Pokémon's type is Darkness until the end of your turn. If that Pokémon is no longer your Active Pokémon, this effect ends.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_weavile_40_dark_engage(), activation=Activations.ONCE_PER_TURN), Attack(title='Shadow Charge', game_text='Search your deck for up to 2 Darkness Energy cards and attach them to any of your Pokémon in any way you like. Shuffle your deck afterward.', cost={}, effect=dp3_weavile_40_shadow_charge()), Attack(title='Chip Off', game_text='If your opponent has 6 or more cards in his or her hand, discard a number of cards without looking until your opponent has 5 cards left in his or her hand.', cost={PokemonTypes.DARKNESS: 2}, damage=40, effect=dp3_weavile_40_chip_off())])
