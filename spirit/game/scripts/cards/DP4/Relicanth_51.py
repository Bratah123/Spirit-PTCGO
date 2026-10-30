"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_relicanth_51_primal_calling,
    dp4_relicanth_51_sleep_swirl,
)

card = PokemonCardDef(guid='29b73313-1fab-5e31-9822-260ceffcacda', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name', display_name='Relicanth', searchable_by=['Relicanth', 'Basic', 'Relicanth'], subtypes=['Basic'], collector_number=51, set_code='DP4', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=369, abilities=[Attack(title='Primal Calling', game_text='Search your deck for up to 3 Trainer Cards that have Fossil in their names, show them to your opponent, and put them into your hand. Shuffle your deck afterward.', cost={}, effect=dp4_relicanth_51_primal_calling()), Attack(title='Sleep Swirl', game_text='Both Relicanth and the Defending Pokémon are now Asleep.', cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=dp4_relicanth_51_sleep_swirl())])
