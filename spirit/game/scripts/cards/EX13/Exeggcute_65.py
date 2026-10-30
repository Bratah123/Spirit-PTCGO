"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    pebble_throw,
)

card = PokemonCardDef(guid='ba542772-e6ac-5b12-be3f-5a5a52051336', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name', display_name='Exeggcute δ', searchable_by=['Exeggcute δ', 'Basic', 'Exeggcute'], subtypes=['Basic'], collector_number=65, set_code='EX13', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=102, abilities=[Attack(title='Rollout', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Pebble Throw', game_text="Choose 1 of your opponent's Benched Pokémon. This attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, effect=pebble_throw(20))])
