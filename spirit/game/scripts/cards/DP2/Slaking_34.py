"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    energetic_impulse,
)
from spirit.game.card_effects.ex import is_active_pokemon

card = PokemonCardDef(guid='f1d10d9c-3245-5224-94e5-af33a554af12', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name', display_name='Slaking', searchable_by=['Slaking', 'Stage 2', 'Slaking'], subtypes=['Stage 2'], collector_number=34, set_code='DP2', rarity=Rarities.Rare, hp=140, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name', family_id=287, abilities=[Ability(title='Energetic Impulse', game_text="Once during your turn (before your attack), if Slaking is your Active Pokémon, you may flip a coin. If heads, Slaking's Lazy Blow attack's base damage is 130 during this turn. If tails, Slaking can't attack or retreat during this turn. (If Slaking is no longer your Active Pokémon, this effect ends.)", ability_type=AbilityTypes.POKE_POWER, effect=energetic_impulse(), activation=Activations.ONCE_PER_TURN, condition=is_active_pokemon), Attack(title='Lazy Blow', cost={PokemonTypes.COLORLESS: 4}, damage=50)])
