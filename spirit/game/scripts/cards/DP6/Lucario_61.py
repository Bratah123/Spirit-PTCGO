"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.dp import (
    dp6_lucario_61_spike_lariat,
)

card = PokemonCardDef(guid='8a830671-1a27-59b8-8325-e897a12f5174', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name', display_name='Lucario', searchable_by=['Lucario', 'Stage 1', 'Lucario'], subtypes=['Stage 1'], collector_number=61, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name', family_id=447, abilities=[Attack(title='Focus Blast', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1}, effect=snipe_attack(30, pool='any')), Attack(title='Spike Lariat', game_text='If the Defending Pokémon already has any damage counters on it, this attack does 60 damage plus 20 more damage.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=60, damage_operator='+', effect=dp6_lucario_61_spike_lariat())])
