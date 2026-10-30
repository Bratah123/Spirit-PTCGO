"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_furret_27_baton_pass,
    dp3_furret_27_keen_eye,
)

card = PokemonCardDef(guid='de279517-388f-5fb8-8b4a-3d8caaceb696', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name', display_name='Furret', searchable_by=['Furret', 'Stage 1', 'Furret'], subtypes=['Stage 1'], collector_number=27, set_code='DP3', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name', family_id=161, abilities=[Attack(title='Keen Eye', game_text='Search your deck for up to 2 cards and put them into your hand. Shuffle your deck afterward.', cost={}, effect=dp3_furret_27_keen_eye()), Attack(title='Baton Pass', game_text='You may switch Furret with 1 of your Benched Pokémon. If you do, move as many Energy cards attached to Furret as you like to the new Active Pokémon.', cost={PokemonTypes.COLORLESS: 2}, damage=40, effect=dp3_furret_27_baton_pass())])
