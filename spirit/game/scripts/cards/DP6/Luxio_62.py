"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.dp import (
    dp6_luxio_62_thunderous_claw,
)

card = PokemonCardDef(guid='9b6858ff-67b0-5b0a-8923-27f5caca7cab', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name', display_name='Luxio', searchable_by=['Luxio', 'Stage 1', 'Luxio'], subtypes=['Stage 1'], collector_number=62, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name', family_id=403, abilities=[Attack(title='Spark', game_text="Does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=snipe_attack(10, also_base=True)), Attack(title='Thunderous Claw', game_text='Flip a coin. If tails, discard all Lightning Energy attached to Luxio.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=70, effect=dp6_luxio_62_thunderous_claw())])
