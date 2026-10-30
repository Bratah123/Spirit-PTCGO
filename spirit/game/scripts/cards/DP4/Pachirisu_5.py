"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_pachirisu_5_call_for_family,
    dp4_pachirisu_5_smash_short,
)

card = PokemonCardDef(guid='1727e451-458f-5fe4-b6e2-c356a52ac787', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name', display_name='Pachirisu', searchable_by=['Pachirisu', 'Basic', 'Pachirisu'], subtypes=['Basic'], collector_number=5, set_code='DP4', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=417, abilities=[Attack(title='Call for Family', game_text='Search your deck for up to 3 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp4_pachirisu_5_call_for_family()), Attack(title='Smash Short', game_text="If the Defending Pokémon has a Pokémon Tool card attached to it, this attack does 10 damage plus 30 more damage. Discard that Pokémon Tool card, look at your opponent's hand, and discard any Pokémon Tool cards of the same name you find there.", cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=dp4_pachirisu_5_smash_short())])
