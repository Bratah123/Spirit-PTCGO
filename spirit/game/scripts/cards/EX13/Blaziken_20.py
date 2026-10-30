"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    blaze_kick,
)

card = PokemonCardDef(guid='671cabca-047f-54dd-ac72-e37c80ad0419', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name', display_name='Blaziken', searchable_by=['Blaziken', 'Stage 2', 'Blaziken'], subtypes=['Stage 2'], collector_number=20, set_code='EX13', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name', family_id=255, abilities=[Attack(title='Combustion', cost={PokemonTypes.FIRE: 1}, damage=30), Attack(title='Blaze Kick', game_text='Flip a coin. If heads, this attack does 40 damage plus 20 more damage. If tails, the Defending Pokémon is now Burned.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=blaze_kick(40, 20))])
