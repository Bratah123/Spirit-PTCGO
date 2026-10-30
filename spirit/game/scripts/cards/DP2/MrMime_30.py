"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    airy_wall_passive,
    trick_play,
)

card = PokemonCardDef(guid='b9c68eaf-caa5-58e4-8790-d1c171e81212', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name', display_name='Mr. Mime', searchable_by=['Mr. Mime', 'Basic', 'MrMime'], subtypes=['Basic'], collector_number=30, set_code='DP2', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=122, abilities=[Ability(title='Airy Wall', game_text="If your opponent's Pokémon that has 2 or less Energy cards attached to it attacks Mr. Mime, prevent all damage done to Mr. Mime from that attack. If Mime Jr. is anywhere under Mr. Mime, prevent all effects of that attack, including damage, done to Mr. Mime.", ability_type=AbilityTypes.POKE_BODY, passive=airy_wall_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Trick Play', game_text="Put a coin next to your Active Pokémon without showing your opponent and cover it with your hand. Your opponent guesses if the coin is heads or tails. If he or she is wrong, this attack does 50 damage to the Defending Pokémon. If he or she is right, Mr. Mime does 20 damage to itself, and this attack's damage isn't affected by Weakness or Resistance.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, effect=trick_play())])
