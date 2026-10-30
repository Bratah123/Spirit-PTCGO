"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(guid='180ff713-7cb6-550f-b03b-edcbe5413f0d', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name', display_name='Metang', searchable_by=['Metang', 'Stage 1', 'Metang'], subtypes=['Stage 1'], collector_number=64, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name', family_id=374, abilities=[Attack(title='Agility', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Metang during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=flip_protection(prevent=True, effects_too=True, title='Agility')), Attack(title='Metal Claw', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=50)])
