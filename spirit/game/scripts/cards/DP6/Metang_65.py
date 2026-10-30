"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp6_metang_65_bullet_punch,
)

card = PokemonCardDef(guid='7891a755-2267-525d-9b8e-cab807e42f10', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name', display_name='Metang', searchable_by=['Metang', 'Stage 1', 'Metang'], subtypes=['Stage 1'], collector_number=65, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name', family_id=374, abilities=[Attack(title='Psyshock', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Bullet Punch', game_text='Flip 2 coins. This attack does 40 damage plus 20 more damage for each heads.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=dp6_metang_65_bullet_punch())])
