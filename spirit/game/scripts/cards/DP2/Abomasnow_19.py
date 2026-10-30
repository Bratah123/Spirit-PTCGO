"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    glacier_snow_passive,
    heavy_blizzard_bench,
)

card = PokemonCardDef(guid='4ea8fa1c-dad9-524a-b9c2-95bd09d8d020', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name', display_name='Abomasnow', searchable_by=['Abomasnow', 'Stage 1', 'Abomasnow'], subtypes=['Stage 1'], collector_number=19, set_code='DP2', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name', family_id=459, abilities=[Ability(title='Glacier Snow', game_text="If Abomasnow is your Active Pokémon and is damaged by an opponent's attack (even if Abomasnow is Knocked Out), the Attacking Pokémon is now Asleep.", ability_type=AbilityTypes.POKE_BODY, passive=glacier_snow_passive()), Attack(title='Heavy Blizzard', game_text="Flip a coin. If heads, put 1 damage counter on each of your opponent's Benched Pokémon.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=heavy_blizzard_bench(10))])
