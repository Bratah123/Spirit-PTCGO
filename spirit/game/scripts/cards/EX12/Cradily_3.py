"""STUB: effect not implemented — do not guess mechanics.
Cradily (EX12 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import (
    devolution_wave_react,
)

card = PokemonCardDef(guid='7efab587-876e-55dd-8758-88dd5fe348c9', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name', display_name='Cradily', searchable_by=['Cradily', 'Stage 2', 'Cradily'], subtypes=['Stage 2'], collector_number=3, set_code='EX12', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name', family_id=345, abilities=[Attack(title='Devolution Wave', game_text="Count the number of React Energy cards attached to Cradily and choose up to that number of your opponent's Evolved Pokémon. Remove the highest Stage Evolution card from each of those Pokémon, then have your opponent shuffle those cards into his or her deck.", cost={PokemonTypes.COLORLESS: 2}, effect=devolution_wave_react()), Attack(title='Linear Attack', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, effect=snipe_attack(30, pool='any')), Attack(title='Mud Shot', cost={PokemonTypes.COLORLESS: 3}, damage=50)])
