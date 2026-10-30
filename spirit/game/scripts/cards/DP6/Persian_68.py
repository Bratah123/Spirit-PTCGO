"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, snipe_attack

card = PokemonCardDef(guid='d4d5737f-a697-5d6f-9a1a-7b45f30b89a7', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name', display_name='Persian', searchable_by=['Persian', 'Stage 1', 'Persian'], subtypes=['Stage 1'], collector_number=68, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name', family_id=52, abilities=[Attack(title='Feint Attack', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.COLORLESS: 2}, effect=snipe_attack(30, pool='any')), Attack(title='Fasten Claws', game_text='Flip a coin. If heads, this attack does 40 damage plus 10 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=flip_bonus(10))])
