"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    crash_bomber,
)
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='e75b45ee-d247-5d2e-b37e-c8c3551e110f', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name', display_name='Octillery', searchable_by=['Octillery', 'Stage 1', 'Octillery'], subtypes=['Stage 1'], collector_number=57, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name', family_id=223, abilities=[Attack(title='Crash Bomber', game_text='If the Defending Pokémon has any Special Energy cards attached to it, this attack does 30 damage plus 30 more damage. Then, discard a Special Energy card attached to the Defending Pokémon.', cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=crash_bomber(30, 30)), Attack(title='Aqua Liner', game_text="Choose 1 of your opponent's Benched Pokémon. This attack does 40 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 2}, effect=snipe_attack(40, pool='bench'))])
