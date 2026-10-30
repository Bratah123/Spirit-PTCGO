"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_glaceonlvx_98_avalanche,
    dp5_glaceonlvx_98_chilly_breath_passive,
)

card = PokemonCardDef(guid='a873f9b6-2e3d-515c-9f1e-24fe8a6ec500', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonLVX.Name', display_name='Glaceon LV.X', searchable_by=['Glaceon LV.X', 'Level-Up', 'GlaceonLVX'], subtypes=['Level-Up'], collector_number=98, set_code='DP5', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.LEVELUP, retreat_cost=1, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name', family_id=133, abilities=[Ability(title='Chilly Breath', game_text="As long as Glaceon is your Active Pokémon, your opponent's Pokémon can't use any Poké-Powers.", ability_type=AbilityTypes.POKE_BODY, passive=dp5_glaceonlvx_98_chilly_breath_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Avalanche', game_text="Flip a coin. If heads, this attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=70, effect=dp5_glaceonlvx_98_avalanche())])
