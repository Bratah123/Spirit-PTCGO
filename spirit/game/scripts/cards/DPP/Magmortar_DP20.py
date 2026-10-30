"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.dp import (
    flame_drum,
)

card = PokemonCardDef(guid='55d4e596-62b2-5015-9473-320ab21ad123', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name', display_name='Magmortar', searchable_by=['Magmortar', 'Stage 1', 'Magmortar'], subtypes=['Stage 1'], collector_number=20, set_code='DP2', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name', family_id=126, abilities=[Attack(title='Smoke Bomb', game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.", cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=smokescreen_attack()), Attack(title='Flame Drum', game_text="If Magby isn't anywhere under Magmortar, discard 2 Energy cards from your hand. (If you can't discard 2 Energy cards from your hand, this attack does nothing.)", cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=80, effect=flame_drum(80))])
