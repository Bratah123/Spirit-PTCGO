"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_blaziken_1_fire_dance,
    dp4_blaziken_1_flame_kick,
)

card = PokemonCardDef(guid='06b55a59-f0b3-5c9d-bc99-62d748a20f97', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name', display_name='Blaziken', searchable_by=['Blaziken', 'Stage 2', 'Blaziken'], subtypes=['Stage 2'], collector_number=1, set_code='DP4', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name', family_id=255, abilities=[Attack(title='Fire Dance', game_text='Search your discard pile for a Fire Energy card and attach it to 1 of your Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=30, effect=dp4_blaziken_1_fire_dance()), Attack(title='Flame Kick', game_text="Discard 2 Fire Energy attached to Blaziken. This attack does 80 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, effect=dp4_blaziken_1_flame_kick())])
