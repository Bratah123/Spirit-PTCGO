"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='376f7cb9-e04a-52ee-91f7-5141ab095c2c', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name', display_name='Toxicroak', searchable_by=['Toxicroak', 'Stage 1', 'Toxicroak'], subtypes=['Stage 1'], collector_number=31, set_code='DP5', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name', family_id=453, abilities=[Attack(title='Paralyze Poison', game_text='The Defending Pokémon is now Poisoned. Flip a coin. If heads, the Defending Pokémon is now Paralyzed and Poisoned.', cost={PokemonTypes.PSYCHIC: 1}, damage=20, effect=condition_attack(SpecialConditions.POISONED, flip=True)), Attack(title='Slash', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60)])
