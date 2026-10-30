"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import split_bomb_snipe
from spirit.game.card_effects.ex import (
    delta_circle,
)

card = PokemonCardDef(guid='16a5a1a0-5d16-5e91-81d3-123424ee6484', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name', display_name='Exeggutor δ', searchable_by=['Exeggutor δ', 'Stage 1', 'Exeggutor'], subtypes=['Stage 1'], collector_number=41, set_code='EX13', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name', family_id=103, abilities=[Attack(title='Delta Circle', game_text='Does 10 damage plus 10 more damage for each Pokémon you have in play that has δ on its card.', cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='+', effect=delta_circle(10, 10)), Attack(title='Split Bomb', game_text="Choose 2 of your opponent's Pokémon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, effect=split_bomb_snipe())])
