"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    fire_counterattack,
    ultra_powder,
)

card = PokemonCardDef(guid='7f46a332-c311-5168-98eb-a43b6197edcc', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name', display_name='Meganium', searchable_by=['Meganium', 'Stage 2', 'Meganium'], subtypes=['Stage 2'], collector_number=13, set_code='DP2', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name', family_id=152, abilities=[Attack(title='Ultra Powder', game_text='Flip 3 coins. If the first coin is heads, the Defending Pokémon is now Poisoned. If the second coin is heads, the Defending Pokémon is now Burned. If the third coin is heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.GRASS: 1}, damage=20, effect=ultra_powder()), Attack(title='Fire Counterattack', game_text='If your opponent has any Fire Pokémon in play, this attack does 60 damage plus 30 more damage.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1}, damage=60, damage_operator='+', effect=fire_counterattack(60, 30))])
