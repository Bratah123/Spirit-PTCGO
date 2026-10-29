from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import lazy_howl

card = PokemonCardDef(guid='7edf8df3-db60-5fa4-a2b4-1bf5ed0cfa34', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name', display_name='Slakoth', searchable_by=['Slakoth', 'Basic', 'Slakoth'], subtypes=['Basic'], collector_number=167, set_code='SM11', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=287, abilities=[Attack(title='Lazy Howl', game_text="During your opponent's next turn, if they attach an Energy card from their hand to the Defending Pokémon, their turn ends.", cost={PokemonTypes.COLORLESS: 1}, effect=lazy_howl), Attack(title='Hang Down', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
