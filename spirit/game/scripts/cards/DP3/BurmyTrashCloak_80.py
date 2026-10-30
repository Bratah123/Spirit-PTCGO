"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_burmytrashcloak_80_trash_cloak_tackle,
    dp3_burmytrashcloak_80_wear_cloak,
)

card = PokemonCardDef(guid='3972b272-38fa-5e8d-abfb-7eee035747cf', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.BurmyTrashCloak.Name', display_name='Burmy Trash Cloak', searchable_by=['Burmy Trash Cloak', 'Basic', 'BurmyTrashCloak'], subtypes=['Basic'], collector_number=80, set_code='DP3', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=412, abilities=[Ability(title='Wear Cloak', game_text='Once during your turn (before your attack), if Burmy Trash Cloak is your Active Pokémon, you may search your discard for a basic Metal Energy card and attach it to Burmy Trash Cloak.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_burmytrashcloak_80_wear_cloak(), activation=Activations.ONCE_PER_TURN), Attack(title='Trash Cloak Tackle', game_text='If Burmy Trash Cloak has any Metal Energy attached to it, this attack does 10 damage plus 10 more damage.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=dp3_burmytrashcloak_80_trash_cloak_tackle())])
