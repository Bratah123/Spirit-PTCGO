"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    electromagnetic_induction,
    explosive_thunder,
)

card = PokemonCardDef(guid='384c5a06-7e1e-5865-b3ab-0e8b00ac0cd4', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name', display_name='Raichu', searchable_by=['Raichu', 'Stage 1', 'Raichu'], subtypes=['Stage 1'], collector_number=21, set_code='DP2', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name', family_id=25, abilities=[Attack(title='Electromagnetic Induction', game_text='Search your deck for up to 2 Lightning Energy cards and attach them to 1 of your Pokémon. Shuffle your deck afterward.', cost={}, effect=electromagnetic_induction()), Attack(title='Explosive Thunder', game_text='Discard all basic Lightning Energy cards attached to Raichu. This attack does 30 damage times the number of Lightning Energy cards you discarded.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='x', effect=explosive_thunder(30))])
