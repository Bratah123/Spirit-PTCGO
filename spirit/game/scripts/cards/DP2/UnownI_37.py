"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    unown_bench_condition,
    unown_i_hidden_power,
    unown_item,
)

card = PokemonCardDef(guid='15b3f46f-38d5-5a6c-87c4-9c638fc9d6d2', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownI.Name', display_name='Unown [I]', searchable_by=['Unown [I]', 'Basic', 'UnownI'], subtypes=['Basic'], collector_number=37, set_code='DP2', rarity=Rarities.Rare, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='ITEM', game_text="Once during your turn (before your attack), if you have Unown I, Unown T, Unown E, and Unown M on your Bench, you may search your deck for a Trainer card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. You can't use more than 1 ITEM Poké-Power each turn.", ability_type=AbilityTypes.POKE_POWER, effect=unown_item(), activation=Activations.ONCE_PER_TURN, condition=unown_bench_condition), Attack(title='Hidden Power', game_text="Choose an Energy card attached to the Defending Pokémon and put it face down. Treat that card as a Special Energy card that provides Colorless Energy and doesn't have any effect other than providing Energy. Put that card face up at the end of your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=unown_i_hidden_power())])
