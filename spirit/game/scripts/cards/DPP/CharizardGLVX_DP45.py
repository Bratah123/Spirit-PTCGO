"""STUB: effect not implemented — do not guess mechanics.
Charizard G LV.X (DPP #DP45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dpp_charizardglvx_dp45_call_for_power,
    dpp_charizardglvx_dp45_malevolent_fire,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='ac133e42-4839-58c2-96fe-0b0fe5edc114', key='DPP', name='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardGLVX.Name', display_name='Charizard G LV.X', searchable_by=['Charizard G LV.X', 'Level-Up', 'SP', 'CharizardGLVX'], subtypes=['Level-Up', 'SP'], collector_number=45, set_code='DPP', rarity=Rarities.RarePromo, hp=120, elements=[PokemonTypes.FIRE], stage=PokemonStage.LEVELUP, retreat_cost=3, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardG.Name', family_id=6, abilities=[Ability(title='Call for Power', game_text="As often as you like during your turn (before your attack), you may move an Energy attached to 1 of your Pokémon to Charizard G. This power can't be used if Charizard G is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dpp_charizardglvx_dp45_call_for_power(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Malevolent Fire', game_text='Flip a coin. If tails, discard all Energy attached to Charizard G.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 3}, damage=150, effect=dpp_charizardglvx_dp45_malevolent_fire())])
