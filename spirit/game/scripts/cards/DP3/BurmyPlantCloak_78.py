"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_burmyplantcloak_78_plant_cloak_tackle,
    dp3_burmyplantcloak_78_wear_cloak,
)

card = PokemonCardDef(guid='0154511a-07fc-5037-8178-c6f4d9f03686', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name', display_name='Burmy Plant Cloak', searchable_by=['Burmy Plant Cloak', 'Basic', 'BurmyPlantCloak'], subtypes=['Basic'], collector_number=78, set_code='DP3', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=412, abilities=[Ability(title='Wear Cloak', game_text='Once during your turn (before your attack), if Burmy Plant Cloak is your Active Pokémon, you may search your discard pile for a basic Grass Energy card and attach it to Burmy Plant Cloak.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_burmyplantcloak_78_wear_cloak(), activation=Activations.ONCE_PER_TURN), Attack(title='Plant Cloak Tackle', game_text='If Burmy Plant Cloak has any Grass Energy attached to it, this attack does 10 damage plus 10 more damage.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=dp3_burmyplantcloak_78_plant_cloak_tackle())])
