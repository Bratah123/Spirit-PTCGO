"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_regigigas_15_crush_grip,
    dp6_regigigas_15_slow_start,
)

card = PokemonCardDef(guid='5fcef6bf-af10-5ba6-8908-df54ff535d80', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name', display_name='Regigigas', searchable_by=['Regigigas', 'Basic', 'Regigigas'], subtypes=['Basic'], collector_number=15, set_code='DP6', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, family_id=486, abilities=[Ability(title='Slow Start', game_text="Regigigas can't attack until your opponent has 3 or less Prize cards left.", ability_type=AbilityTypes.POKE_BODY, effect=dp6_regigigas_15_slow_start(), activation=Activations.ONCE_PER_TURN), Attack(title='Crush Grip', game_text="If the Defending Pokémon already has any damage counters on it, this attack's base damage is 40 instead of 120.", cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=120, effect=dp6_regigigas_15_crush_grip())])
