from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import turn_the_tables

card = PokemonCardDef(guid='3d568bf7-0890-5f4d-af93-665437fbb5d0', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name', display_name='Heracross', searchable_by=['Heracross', 'Basic', 'Heracross'], subtypes=['Basic'], collector_number=107, set_code='SM11', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=214, abilities=[Attack(title='Turn the Tables', game_text="If 1 of your opponent's Pokémon used a GX attack during their last turn, your opponent shuffles their Active Pokémon and all cards attached to it into their deck.", cost={PokemonTypes.COLORLESS: 1}, effect=turn_the_tables), Attack(title='Tackle', cost={PokemonTypes.COLORLESS: 3}, damage=70)])
