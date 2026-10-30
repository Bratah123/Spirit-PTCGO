"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    happy_chance,
    kind_egg_condition,
    kind_egg_power,
)

card = PokemonCardDef(guid='f26c706b-c7d2-5050-8ed9-ca74a6ce9d9b', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name', display_name='Blissey', searchable_by=['Blissey', 'Stage 1', 'Blissey'], subtypes=['Stage 1'], collector_number=5, set_code='DP2', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name', family_id=113, abilities=[Ability(title='Kind Egg', game_text="Once during your turn (before your attack), if Happiny is anywhere under Blissey, you may choose a number of cards in your hand up to the amount of Energy attached to Blissey and put those cards on top of your deck. Shuffle your deck afterward. Then, draw that many cards. This power can't be used if Blissey is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=kind_egg_power(), activation=Activations.ONCE_PER_TURN, condition=kind_egg_condition), Attack(title='Happy Chance', game_text='Does 20 damage plus 10 for each Energy attached to Blissey. Before doing damage, you may search your discard pile for a basic Energy card and attach it to Blissey.', cost={PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=happy_chance(20))])
