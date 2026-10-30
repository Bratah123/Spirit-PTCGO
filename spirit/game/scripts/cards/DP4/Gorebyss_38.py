"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_gorebyss_38_sweet_temptation,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='b196182f-dcea-5105-93cc-3f3952e55cb1', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name', display_name='Gorebyss', searchable_by=['Gorebyss', 'Stage 1', 'Gorebyss'], subtypes=['Stage 1'], collector_number=38, set_code='DP4', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name', family_id=366, abilities=[Attack(title='Sweet Temptation', game_text="Switch 1 of your opponent's Benched Pokémon with 1 of the Defending Pokémon. This attack does 10 damage to the new Defending Pokémon.", cost={}, effect=dp4_gorebyss_38_sweet_temptation()), Attack(title='Psychic Snap', game_text='If Gorebyss has any Psychic Energy attached to it, this attack does 30 damage plus 20 more damage and the Defending Pokémon is now Confused.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=condition_attack(SpecialConditions.CONFUSED))])
