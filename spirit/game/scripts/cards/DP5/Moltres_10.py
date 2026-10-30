"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_moltres_10_flame_charge,
    dp5_moltres_10_scorching_wing,
)

card = PokemonCardDef(guid='00cc2183-b096-5b9a-9dde-e09e2f7f233b', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name', display_name='Moltres', searchable_by=['Moltres', 'Basic', 'Moltres'], subtypes=['Basic'], collector_number=10, set_code='DP5', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=146, abilities=[Ability(title='Flame Charge', game_text='Once during your turn, when you put Moltres from your hand onto your Bench, you may flip a coin. If heads, search your discard pile for up to 3 Fire Energy cards and attach them to Moltres.', ability_type=AbilityTypes.POKE_POWER, effect=dp5_moltres_10_flame_charge(), activation=Activations.ONCE_PER_TURN), Attack(title='Scorching Wing', game_text='Discard all Fire Energy attached to Moltres.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=100, effect=dp5_moltres_10_scorching_wing())])
