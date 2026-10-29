from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import alert_headbutt

card = PokemonCardDef(guid='65803671-e974-5afc-bb81-4769ed0ce4e3', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name', display_name='Gumshoos', searchable_by=['Gumshoos', 'Stage 1', 'Gumshoos'], subtypes=['Stage 1'], collector_number=181, set_code='SM11', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name', family_id=734, abilities=[Attack(title='Alert Headbutt', game_text="If your opponent's Active Pokémon is a Pokémon-GX or Pokémon-EX, this attack's base damage is 30.", cost={PokemonTypes.COLORLESS: 2}, damage=90, effect=alert_headbutt)])
