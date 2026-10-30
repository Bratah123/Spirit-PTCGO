"""STUB: effect not implemented — do not guess mechanics.
Clamperl (EX12 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    iron_defense_flip,
)

card = PokemonCardDef(guid='02a3371f-0df1-5352-86f3-8e82c20eea73', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name', display_name='Clamperl', searchable_by=['Clamperl', 'Basic', 'Clamperl'], subtypes=['Basic'], collector_number=51, set_code='EX12', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=366, abilities=[Attack(title='Iron Defense', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Clamperl during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=iron_defense_flip()), Attack(title='Clamp Splash', cost={PokemonTypes.WATER: 1}, damage=10)])
