"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    mud_spit_snipe,
)

card = PokemonCardDef(guid='d44cff58-1022-55ee-b024-06d97c6d571c', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name', display_name='Barboach', searchable_by=['Barboach', 'Basic', 'Barboach'], subtypes=['Basic'], collector_number=72, set_code='DP2', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=339, abilities=[Attack(title='Mud Spit', game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1}, effect=mud_spit_snipe(10))])
