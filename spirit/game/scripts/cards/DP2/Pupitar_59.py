"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import breaking_sound
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='8e57f3b6-7a2d-5d74-9350-e43590c92665', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name', display_name='Pupitar', searchable_by=['Pupitar', 'Stage 1', 'Pupitar'], subtypes=['Stage 1'], collector_number=59, set_code='DP2', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name', family_id=246, abilities=[Attack(title='Pressurized Gas', game_text="Does 10 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 2}, effect=breaking_sound(10)), Attack(title='Rocket Tackle', game_text="Pupitar does 10 damage to itself. Flip a coin. If heads, prevent all damage done to Pupitar by attacks during your opponent's next turn.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=recoil_attack(10, damage=50))])
