"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_wormadamtrashcloak_43_trash_cloak,
)
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='111bfa50-34d2-507f-ad29-d38dc10a6af0', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.WormadamTrashCloak.Name', display_name='Wormadam Trash Cloak', searchable_by=['Wormadam Trash Cloak', 'Stage 1', 'WormadamTrashCloak'], subtypes=['Stage 1'], collector_number=43, set_code='DP3', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.BurmyTrashCloak.Name', family_id=412, abilities=[Ability(title='Trash Cloak', game_text='If Wormadam Trash Cloak has a Pokémon Tool card attached to it, any damage done to Wormadam Trash Cloak by attacks is reduced by 20 (after applying Weakness and Resistance).', ability_type=AbilityTypes.POKE_BODY, effect=dp3_wormadamtrashcloak_43_trash_cloak(), activation=Activations.ONCE_PER_TURN), Attack(title='Iron Tackle', game_text='Wormadam Trash Cloak does 20 damage to itself.', cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1}, damage=70, effect=recoil_attack(20, damage=70))])
