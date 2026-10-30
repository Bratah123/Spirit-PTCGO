"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import foresight_reorder
from spirit.game.card_effects.ex import (
    overrun_bench,
)

card = PokemonCardDef(guid='b1e0f447-2728-5474-adbd-e027cc5a5d57', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name', display_name='Absol', searchable_by=['Absol', 'Basic', 'Absol'], subtypes=['Basic'], collector_number=18, set_code='EX13', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, family_id=359, abilities=[Attack(title='Foresight', game_text="Look at the top 5 cards of either player's deck and put them back on top of that player's deck in any order.", cost={PokemonTypes.COLORLESS: 1}, effect=foresight_reorder()), Attack(title='Overrun', game_text="Choose 1 of your opponent's Benched Pokémon. This attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, damage=10, effect=overrun_bench(10, 20))])
