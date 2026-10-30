"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_kabuto_67_ancient_guidance,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='71874857-0603-507d-8cf0-36476467d769', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name', display_name='Kabuto', searchable_by=['Kabuto', 'Stage 1', 'Kabuto'], subtypes=['Stage 1'], collector_number=67, set_code='DP5', rarity=Rarities.Common, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.DomeFossil.Name', family_id=140, abilities=[Ability(title='Ancient Guidance', game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for Helix Fossil, Dome Fossil, or Old Amber and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Kabuto is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp5_kabuto_67_ancient_guidance(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Shell Attack', cost={PokemonTypes.FIGHTING: 1}, damage=20)])
