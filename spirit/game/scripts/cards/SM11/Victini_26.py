from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import victory_sign

card = PokemonCardDef(guid='429e1036-d0ec-5f87-9ba4-20340784dcc8', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name', display_name='Victini', searchable_by=['Victini', 'Basic', 'Victini'], subtypes=['Basic'], collector_number=26, set_code='SM11', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=494, abilities=[Attack(title='Victory Sign', game_text='Search your deck for up to 2 basic Energy cards of different types and attach them to your Pokémon in any way you like. Then, shuffle your deck.', cost={PokemonTypes.FIRE: 1}, effect=victory_sign), Attack(title='Flare', cost={PokemonTypes.FIRE: 1}, damage=20)])
