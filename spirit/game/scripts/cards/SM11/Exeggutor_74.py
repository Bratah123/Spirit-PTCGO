from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm11 import full_clean

card = PokemonCardDef(guid='ca7bfa41-3069-5b0e-b734-3272a9bfdc9b', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name', display_name='Exeggutor', searchable_by=['Exeggutor', 'Stage 1', 'Exeggutor'], subtypes=['Stage 1'], collector_number=74, set_code='SM11', rarity=Rarities.Rare, hp=140, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name', family_id=102, abilities=[Attack(title='Mind Bend', game_text="Your opponent's Active Pokémon is now Confused.", cost={PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.CONFUSED)), Attack(title='Full Clean', game_text='Discard your hand.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=180, effect=full_clean)])
