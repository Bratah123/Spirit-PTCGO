"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_unownf_56_fake,
)
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='f5647ea8-68c0-589e-a619-6c4363471e84', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownF.Name', display_name='Unown [F]', searchable_by=['Unown [F]', 'Basic', 'UnownF'], subtypes=['Basic'], collector_number=56, set_code='DP4', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='FAKE', game_text='Once during your turn (before your attack), if Unown F is on your Bench, you may use this power. Put a coin next to your Active Pokémon without showing your opponent and cover it with your hand. Your opponent guesses if the coin is heads or tails. If he or she is wrong, draw a card.', ability_type=AbilityTypes.POKE_POWER, effect=dp4_unownf_56_fake(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text="You may flip a coin. If tails, this attack does nothing. If heads, this attack's base damage is 30.", cost={PokemonTypes.PSYCHIC: 1}, damage=10, effect=flip_or_nothing())])
