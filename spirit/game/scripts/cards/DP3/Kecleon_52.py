"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_kecleon_52_camouflage,
)
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='f2ea9c7c-02ab-5ae9-967e-bfd28918eaba', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name', display_name='Kecleon', searchable_by=['Kecleon', 'Basic', 'Kecleon'], subtypes=['Basic'], collector_number=52, set_code='DP3', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=352, abilities=[Ability(title='Camouflage', game_text="If any basic Energy card attached to Kecleon is the same as the Attacking Pokémon's type, any damage done by attacks from the Pokémon to Kecleon is reduced by 40 (after applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=dp3_kecleon_52_camouflage(), activation=Activations.ONCE_PER_TURN), Attack(title='Blind Scratch', game_text="Flip a coin. If tails, this attack does no damage to the Defending Pokémon. Instead, this attack does 20 damage to 1 of your Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 2}, damage=60, effect=flip_or_nothing())])
