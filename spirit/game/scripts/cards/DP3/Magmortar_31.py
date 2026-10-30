"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_magmortar_31_fireball_bazooka,
    dp3_magmortar_31_flame_blast,
    dp3_magmortar_31_flame_body,
)

card = PokemonCardDef(guid='f93e728c-e8d4-5f22-a1f7-949208e97fab', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name', display_name='Magmortar', searchable_by=['Magmortar', 'Stage 1', 'Magmortar'], subtypes=['Stage 1'], collector_number=31, set_code='DP3', rarity=Rarities.Rare, hp=110, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name', family_id=126, abilities=[Ability(title='Flame Body', game_text='When you attach a Fire Energy card from your hand to Magmortar, remove 2 damage counters from Magmortar.', ability_type=AbilityTypes.POKE_BODY, effect=dp3_magmortar_31_flame_body(), activation=Activations.ONCE_PER_TURN), Attack(title='Flame Blast', game_text='Does 20 damage times the number of Fire Energy attached to Magmortar.', cost={PokemonTypes.FIRE: 1}, damage=20, damage_operator='x', effect=dp3_magmortar_31_flame_blast()), Attack(title='Fireball Bazooka', game_text="Does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=40, effect=dp3_magmortar_31_fireball_bazooka())])
