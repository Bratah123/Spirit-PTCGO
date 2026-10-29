from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.sm11 import luminous_blade

card = PokemonCardDef(guid='ff60b942-4a76-5540-9d5c-adba918a771f', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name', display_name='Cresselia', searchable_by=['Cresselia', 'Basic', 'Cresselia'], subtypes=['Basic'], collector_number=87, set_code='SM11', rarity=Rarities.Uncommon, hp=130, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=488, abilities=[Attack(title='Aurora Gain', game_text='Heal 30 damage from this Pokémon.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=heal_attack(30)), Attack(title='Luminous Blade', game_text='Discard a Psychic Energy from this Pokémon.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2}, damage=130, effect=luminous_blade)])
