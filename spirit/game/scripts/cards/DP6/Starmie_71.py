"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_starmie_71_star_boomerang,
)
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='e62b0f90-249a-5a5a-8718-864e6155d7e7', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name', display_name='Starmie', searchable_by=['Starmie', 'Stage 1', 'Starmie'], subtypes=['Stage 1'], collector_number=71, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name', family_id=120, abilities=[Attack(title='Star Boomerang', game_text='You may return Starmie and all cards attached to it to your hand.', cost={PokemonTypes.WATER: 1}, damage=30, effect=dp6_starmie_71_star_boomerang()), Attack(title='Core Flash', game_text="Choose 1 of your opponent's Pokémon that has any Poké-Powers or Poké-Bodies. This attack does 50 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.PSYCHIC: 1}, effect=snipe_attack(50, pool='bench'))])
