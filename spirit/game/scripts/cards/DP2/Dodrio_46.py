"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    triple_pick_evolved_snipe,
)
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(guid='cddc897c-1758-5f21-8c4c-26dd71224a7b', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name', display_name='Dodrio', searchable_by=['Dodrio', 'Stage 1', 'Dodrio'], subtypes=['Stage 1'], collector_number=46, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name', family_id=84, abilities=[Attack(title='Fury Attack', game_text='Flip 3 coins. This attack does 10 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flip_damage(3, per_heads=10)), Attack(title='Triple Pick', game_text="Choose 3 of your opponent's Evolved Pokémon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 3}, effect=triple_pick_evolved_snipe(30, 3))])
