"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    dp4_cacturne_34_needle_arm,
)

card = PokemonCardDef(guid='b6976c71-9274-517a-8dad-0e7d01603948', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name', display_name='Cacturne', searchable_by=['Cacturne', 'Stage 1', 'Cacturne'], subtypes=['Stage 1'], collector_number=34, set_code='DP4', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name', family_id=331, abilities=[Attack(title='Pin Missile', game_text='Flip 3 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=flip_damage(coins=3, per_heads=20)), Attack(title='Needle Arm', game_text='If the Defending Pokémon already has any damage counters on it, this attack does 50 damage plus 20 more damage.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=dp4_cacturne_34_needle_arm())])
