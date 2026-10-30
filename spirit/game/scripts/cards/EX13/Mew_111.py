"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    super_psywave_snipe,
)

card = PokemonCardDef(guid='4fe7bff0-933f-5871-a7cc-d9404df23eb8', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name', display_name='Mew', searchable_by=['Mew', 'Basic', 'Mew'], subtypes=['Basic'], collector_number=111, set_code='EX13', rarity=Rarities.RareSecret, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=151, abilities=[Attack(title='Super Psywave', game_text="Choose 1 of your opponent's Pokémon. Count the amount of Energy attached to that Pokémon. Put that many damage counters on the Pokémon.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, effect=super_psywave_snipe())])
