"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.dp import (
    dp5_infernape_22_mega_bravo,
)

card = PokemonCardDef(guid='e4ee8c40-4ac5-5d68-9299-6af90d31cb9c', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name', display_name='Infernape', searchable_by=['Infernape', 'Stage 2', 'Infernape'], subtypes=['Stage 2'], collector_number=22, set_code='DP5', rarity=Rarities.Rare, hp=110, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name', family_id=390, abilities=[Attack(title='Mach Punch', game_text="Does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 1}, damage=30, effect=snipe_attack(10, also_base=True)), Attack(title='Mega Bravo', game_text='Discard all Fire Energy attached to Infernape. This attack does 40 damage times the amount of Fire Energy you discarded.', cost={PokemonTypes.FIRE: 1}, damage=40, damage_operator='x', effect=dp5_infernape_22_mega_bravo())])
