from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import cleaning_up

card = PokemonCardDef(guid='107ff3f7-be0b-5bd6-b988-b28468037856', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name', display_name='Purrloin', searchable_by=['Purrloin', 'Basic', 'Purrloin'], subtypes=['Basic'], collector_number=135, set_code='SM11', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=509, abilities=[Attack(title='Cleaning Up', game_text="Discard a Pokémon Tool card from 1 of your opponent's Pokémon.", cost={PokemonTypes.COLORLESS: 1}, effect=cleaning_up)])
