from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.sm11 import tag_impact

card = PokemonCardDef(guid='0cfd8f6e-3a66-511f-bfcd-be61bdae9515', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name', display_name='Kangaskhan', searchable_by=['Kangaskhan', 'Basic', 'Kangaskhan'], subtypes=['Basic'], collector_number=163, set_code='SM11', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=115, abilities=[Attack(title='Double Draw', game_text='Draw 2 cards.', cost={PokemonTypes.COLORLESS: 1}, effect=draw_attack(2)), Attack(title='Tag Impact', game_text='This attack does 50 damage for each of your TAG TEAM Pokémon in play.', cost={PokemonTypes.COLORLESS: 4}, damage=50, damage_operator='x', effect=tag_impact)])
