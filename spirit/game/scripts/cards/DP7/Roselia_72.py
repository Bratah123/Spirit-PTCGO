"""STUB: effect not implemented — do not guess mechanics.
Roselia (DP7 #72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_roselia_72_petal_spikes,
)

card = PokemonCardDef(guid='2718bd66-4fd7-56bb-a9fc-2afb42ef6ed0', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name', display_name='Roselia', searchable_by=['Roselia', 'Basic', 'Roselia'], subtypes=['Basic'], collector_number=72, set_code='DP7', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=315, abilities=[Attack(title='Headbutt', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Petal Spikes', game_text='Flip a coin. If heads, the Defending Pokémon is now Asleep and Poisoned. If Budew is anywhere under Roselia, the Defending Pokémon is now Asleep and Poisoned.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=dp7_roselia_72_petal_spikes())])
