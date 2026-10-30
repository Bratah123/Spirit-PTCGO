"""STUB: effect not implemented — do not guess mechanics.
Duskull (DP7 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_duskull_59_silhouette,
)

card = PokemonCardDef(guid='ab97b386-c4f1-5010-8925-0fcf02e9ea1a', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name', display_name='Duskull', searchable_by=['Duskull', 'Basic', 'Duskull'], subtypes=['Basic'], collector_number=59, set_code='DP7', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=355, abilities=[Attack(title='Silhouette', game_text='Put 1 damage counter on the Defending Pokémon. If the Defending Pokémon already has any damage counters on it, put 2 damage counters on that Pokémon instead.', cost={PokemonTypes.PSYCHIC: 1}, effect=dp7_duskull_59_silhouette()), Attack(title="Will-o'-the-wisp", cost={PokemonTypes.COLORLESS: 2}, damage=20)])
