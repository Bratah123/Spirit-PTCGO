"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    chain_lightning,
    lightning_twister,
)

card = PokemonCardDef(guid='1571b358-50c6-5544-8b3c-1d95de20a862', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name', display_name='Manectric', searchable_by=['Manectric', 'Stage 1', 'Manectric'], subtypes=['Stage 1'], collector_number=28, set_code='DP2', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name', family_id=309, abilities=[Attack(title='Lightning Twister', game_text='Does 20 damage times the number of basic Energy cards attached to Manectric.', cost={PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='x', effect=lightning_twister(20)), Attack(title='Chain Lightning', game_text="Does 20 damage to each of your opponent's Benched Pokémon that is the same type as the Defending Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 3}, damage=70, effect=chain_lightning(70, 20))])
