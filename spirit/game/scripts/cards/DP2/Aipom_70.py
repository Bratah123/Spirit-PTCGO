"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    throw_off_tools_stadium,
)

card = PokemonCardDef(guid='5472cf89-bb1d-5dcc-8413-ced24732604b', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name', display_name='Aipom', searchable_by=['Aipom', 'Basic', 'Aipom'], subtypes=['Basic'], collector_number=70, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=190, abilities=[Attack(title='Tail Whap', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Throw Off', game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Before doing damage, discard all Pokémon Tool cards attached to that Pokémon.", cost={PokemonTypes.COLORLESS: 2}, effect=throw_off_tools_stadium())])
