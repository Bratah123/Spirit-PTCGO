"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    pulse_search,
)

card = PokemonCardDef(guid='ab78fef7-9560-56f2-8fdd-d6e522e6b5ce', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name', display_name='Golbat', searchable_by=['Golbat', 'Stage 1', 'Golbat'], subtypes=['Stage 1'], collector_number=50, set_code='DP2', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name', family_id=41, abilities=[Attack(title='Pulse Search', game_text="Look at your opponent's hand.", cost={PokemonTypes.PSYCHIC: 1}, damage=30, effect=pulse_search(30))])
