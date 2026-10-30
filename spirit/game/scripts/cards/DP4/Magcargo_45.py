"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_magcargo_45_magma_armor,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='110b27fc-d8b8-53e5-99b6-812f72d0e920', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name', display_name='Magcargo', searchable_by=['Magcargo', 'Stage 1', 'Magcargo'], subtypes=['Stage 1'], collector_number=45, set_code='DP4', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name', family_id=218, abilities=[Ability(title='Magma Armor', game_text="Magcargo can't be Asleep or Paralyzed.", ability_type=AbilityTypes.POKE_BODY, effect=dp4_magcargo_45_magma_armor(), activation=Activations.ONCE_PER_TURN), Attack(title='Lava Plume', game_text='You may discard the top card of your deck. If you do, the Defending Pokémon is now Burned.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=condition_attack(SpecialConditions.BURNED))])
