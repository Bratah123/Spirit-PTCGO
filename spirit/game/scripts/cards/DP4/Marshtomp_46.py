"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_marshtomp_46_muddy_bomb,
)

card = PokemonCardDef(guid='a1d22aee-08f6-557d-a082-a99e3467295f', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name', display_name='Marshtomp', searchable_by=['Marshtomp', 'Stage 1', 'Marshtomp'], subtypes=['Stage 1'], collector_number=46, set_code='DP4', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name', family_id=258, abilities=[Attack(title='Pound', cost={PokemonTypes.COLORLESS: 2}, damage=20), Attack(title='Muddy Bomb', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon and 10 damage to each of your opponent's other Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, effect=dp4_marshtomp_46_muddy_bomb())])
