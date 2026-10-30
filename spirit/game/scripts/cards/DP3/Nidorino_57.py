"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp3_nidorino_57_spirited_drill,
)

card = PokemonCardDef(guid='dc7c0438-e540-5d4f-ab6a-d769a4ab7b00', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name', display_name='Nidorino', searchable_by=['Nidorino', 'Stage 1', 'Nidorino'], subtypes=['Stage 1'], collector_number=57, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name', family_id=32, abilities=[Attack(title='Spirited Drill', game_text="During your next turn, each of Nidorino's attacks does 20 more damage to the Defending Pokémon (before applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=dp3_nidorino_57_spirited_drill()), Attack(title='Poison Horn', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=40, effect=condition_attack(SpecialConditions.POISONED))])
