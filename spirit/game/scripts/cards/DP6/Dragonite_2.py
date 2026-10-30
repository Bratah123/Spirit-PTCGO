"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp3_vibrava_74_hyper_beam
from spirit.game.card_effects.dp import (
    dp6_dragonite_2_draco_meteor,
)

card = PokemonCardDef(guid='3ee89cc3-3935-5393-a219-099cb7e98b67', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name', display_name='Dragonite', searchable_by=['Dragonite', 'Stage 2', 'Dragonite'], subtypes=['Stage 2'], collector_number=2, set_code='DP6', rarity=Rarities.RareHolo, hp=140, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name', family_id=147, abilities=[Attack(title='Hyper Beam', game_text='Flip a coin. If heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.COLORLESS: 3}, damage=40, effect=dp3_vibrava_74_hyper_beam()), Attack(title='Draco Meteor', game_text="Flip a coin for each of your opponent's Pokémon. If that coin flip is heads, this attack does 50 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 4}, effect=dp6_dragonite_2_draco_meteor())])
