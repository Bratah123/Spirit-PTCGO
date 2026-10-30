"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    mend_metal_heal,
)

card = PokemonCardDef(guid='e17e7cb8-b887-57ad-bad1-e895a611645b', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name', display_name='Lairon', searchable_by=['Lairon', 'Stage 1', 'Lairon'], subtypes=['Stage 1'], collector_number=53, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name', family_id=304, abilities=[Attack(title='Mend', game_text='Search your discard pile for a Metal Energy card and attach it to Lairon. If you do, remove 2 damage counters from Lairon.', cost={PokemonTypes.METAL: 1}, effect=mend_metal_heal(2)), Attack(title='Confront', cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1}, damage=50)])
