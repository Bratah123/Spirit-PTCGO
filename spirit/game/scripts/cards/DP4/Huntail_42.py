"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_huntail_42_scary_face,
    dp4_huntail_42_threaten_and_drop,
)

card = PokemonCardDef(guid='98ebe38e-58ab-5d4e-a425-d489c6f43d39', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name', display_name='Huntail', searchable_by=['Huntail', 'Stage 1', 'Huntail'], subtypes=['Stage 1'], collector_number=42, set_code='DP4', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name', family_id=366, abilities=[Attack(title='Scary Face', game_text="Flip a coin. If heads, the Defending Pokémon can't attack or retreat during your opponent's next turn.", cost={}, effect=dp4_huntail_42_scary_face()), Attack(title='Threaten and Drop', game_text='If Huntail has any Darkness Energy attached to it, this attack does 30 damage plus 20 more damage and discard a Special Energy card, if any, attached to the Defending Pokémon.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=dp4_huntail_42_threaten_and_drop())])
