"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_unowng_57_guard,
    dp4_unowng_57_hidden_power,
)

card = PokemonCardDef(guid='72022a30-9066-5160-b6dc-4fb7ca311bec', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownG.Name', display_name='Unown [G]', searchable_by=['Unown [G]', 'Basic', 'UnownG'], subtypes=['Basic'], collector_number=57, set_code='DP4', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='GUARD', game_text='Once during your turn (before your attack), if Unown G is on your Bench, you may discard all cards attached to Unown G and attach Unown G to 1 of your Pokémon as a Pokémon Tool card. As long as Unown G is attached to a Pokémon, prevent all effects of attacks, excluding damage, done to that Pokémon.', ability_type=AbilityTypes.POKE_POWER, effect=dp4_unowng_57_guard(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text="If Unown G has any damage counters on it, this attack's base damage is 10.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=dp4_unowng_57_hidden_power())])
