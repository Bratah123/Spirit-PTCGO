"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_houndoom_57_bright_flame,
    dp6_houndoom_57_burning_sensation,
    dp6_houndoom_57_revenge_fang,
)

card = PokemonCardDef(guid='13aa6d13-62b6-5b6d-99cc-cd127aaa1b81', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name', display_name='Houndoom', searchable_by=['Houndoom', 'Stage 1', 'Houndoom'], subtypes=['Stage 1'], collector_number=57, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name', family_id=228, abilities=[Ability(title='Revenge Fang', game_text="If you have less Benched Pokémon than your opponent, each of Houndoom's attacks does 40 more damage to the Active Pokémon (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=dp6_houndoom_57_revenge_fang(), activation=Activations.ONCE_PER_TURN), Attack(title='Burning Sensation', game_text='If the Defending Pokémon already has any damage counters on it, the Defending Pokémon is now Burned.', cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=dp6_houndoom_57_burning_sensation()), Attack(title='Bright Flame', game_text='Flip a coin. If tails, discard 2 Fire Energy attached to Houndoom.', cost={PokemonTypes.FIRE: 2}, damage=60, effect=dp6_houndoom_57_bright_flame())])
