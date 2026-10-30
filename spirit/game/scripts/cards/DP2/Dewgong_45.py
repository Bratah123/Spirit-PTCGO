"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    cold_fat_passive,
    collapse_asleep,
)

card = PokemonCardDef(guid='2759402c-a0ee-56a5-b569-246f17319fb1', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name', display_name='Dewgong', searchable_by=['Dewgong', 'Stage 1', 'Dewgong'], subtypes=['Stage 1'], collector_number=45, set_code='DP2', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name', family_id=86, abilities=[Ability(title='Cold Fat', game_text='As long as Dewgong is Asleep, any damage done to Dewgong by attacks is reduced by 40 (after applying Weakness and Resistance).', ability_type=AbilityTypes.POKE_BODY, passive=cold_fat_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Collapse', game_text='Dewgong is now Asleep.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=collapse_asleep(60))])
