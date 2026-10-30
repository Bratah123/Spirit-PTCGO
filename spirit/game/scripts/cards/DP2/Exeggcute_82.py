"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    direct_hit_bomb_flip_snipe,
)

card = PokemonCardDef(guid='74c87567-2b4f-5a6f-b51f-9325e028fba0', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name', display_name='Exeggcute', searchable_by=['Exeggcute', 'Basic', 'Exeggcute'], subtypes=['Basic'], collector_number=82, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=102, abilities=[Attack(title='Direct-hit Bomb', game_text="Flip a coin for each Energy attached to Exeggcute. Choose 1 of your opponent's Pokémon. For each heads, this attack does 10 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.GRASS: 1}, effect=direct_hit_bomb_flip_snipe(10))])
