"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_politoed_12_enthusiasm,
)
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(guid='2b2bfd82-ed92-56e5-a6c1-31ba9259a26c', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name', display_name='Politoed', searchable_by=['Politoed', 'Stage 2', 'Politoed'], subtypes=['Stage 2'], collector_number=12, set_code='DP6', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name', family_id=60, abilities=[Ability(title='Enthusiasm', game_text="If you have Poliwag, Poliwhirl, and Poliwrath in play, each of these Pokémon's attacks does 60 more damage to the Defending Pokémon (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=dp6_politoed_12_enthusiasm(), activation=Activations.ONCE_PER_TURN), Attack(title='Frog Hop', game_text='Flip a coin. If heads, this attack does 40 damage plus 40 more damage.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=flip_bonus(40))])
