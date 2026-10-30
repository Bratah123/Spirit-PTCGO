"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_wormadamplantcloak_41_plant_cloak,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='39645db9-f55d-57e9-be2b-e41f1a94cc86', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.WormadamPlantCloak.Name', display_name='Wormadam Plant Cloak', searchable_by=['Wormadam Plant Cloak', 'Stage 1', 'WormadamPlantCloak'], subtypes=['Stage 1'], collector_number=41, set_code='DP3', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name', family_id=412, abilities=[Ability(title='Plant Cloak', game_text='If Wormadam Plant Cloak has 2 or more Grass Energy attached to it, Wormadam Plant Cloak gets +40 HP.', ability_type=AbilityTypes.POKE_BODY, effect=dp3_wormadamplantcloak_41_plant_cloak(), activation=Activations.ONCE_PER_TURN), Attack(title='Leaf Hurricane', game_text='If the Defending Pokémon has fewer remaining HP than Wormadam Plant Cloak, the Defending Pokémon is now Confused.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=condition_attack(SpecialConditions.CONFUSED))])
