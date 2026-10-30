"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    unown_m_hidden_power,
    unown_magnet,
)
from spirit.game.card_effects.ex import is_active_pokemon

card = PokemonCardDef(guid='ffc5b89c-e0d9-573e-98e3-1deaf0cfc197', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownM.Name', display_name='Unown [M]', searchable_by=['Unown [M]', 'Basic', 'UnownM'], subtypes=['Basic'], collector_number=66, set_code='DP2', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='MAGNET', game_text="Once during your turn (before your attack), if Unown M is your Active Pokémon, you may flip a coin. If heads, switch 1 of your opponent's Benched Pokémon with 1 of the Defending Pokémon. This power can't be used if Unown M is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=unown_magnet(), activation=Activations.ONCE_PER_TURN, condition=is_active_pokemon), Attack(title='Hidden Power', game_text="Flip a coin. If heads, this attack does 30 damage. If tails, this attack does 30 damage to 1 of your Pokémon, and this attack's damage isn't affected by Weakness or Resistance.", cost={PokemonTypes.COLORLESS: 1}, effect=unown_m_hidden_power())])
