"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_burmysandycloak_79_sandy_cloak_tackle,
    dp3_burmysandycloak_79_wear_cloak,
)

card = PokemonCardDef(guid='6b2c124b-a2d6-51c1-b0eb-6df466286914', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.BurmySandyCloak.Name', display_name='Burmy Sandy Cloak', searchable_by=['Burmy Sandy Cloak', 'Basic', 'BurmySandyCloak'], subtypes=['Basic'], collector_number=79, set_code='DP3', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=412, abilities=[Ability(title='Wear Cloak', game_text='Once during your turn (before your attack), if Burmy Sandy Cloak is your Active Pokémon, you may search your discard for a basic Fighting Energy card and attach it to Burmy Sandy Cloak.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_burmysandycloak_79_wear_cloak(), activation=Activations.ONCE_PER_TURN), Attack(title='Sandy Cloak Tackle', game_text='If Burmy Sandy Cloak has any Fighting Energy attached to it, this attack does 10 damage plus 10 more damage.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=dp3_burmysandycloak_79_sandy_cloak_tackle())])
