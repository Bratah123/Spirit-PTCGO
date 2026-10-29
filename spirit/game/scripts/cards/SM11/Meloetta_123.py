from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.sm11 import tag_cheer

card = PokemonCardDef(guid='0e5a44f9-1864-5dff-b8ab-e787f1d6b6ed', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name', display_name='Meloetta', searchable_by=['Meloetta', 'Basic', 'Meloetta'], subtypes=['Basic'], collector_number=123, set_code='SM11', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=648, abilities=[Attack(title='Tag Cheer', game_text='Attach an Energy card from your hand to 1 of your TAG TEAM Pokémon.', cost={PokemonTypes.COLORLESS: 1}, effect=tag_cheer), Attack(title='Shooting Star Pirouette', game_text='Flip a coin until you get tails. This attack does 30 more damage for each heads.', cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=flip_damage(until_tails=True, bonus_per_heads=30))])
