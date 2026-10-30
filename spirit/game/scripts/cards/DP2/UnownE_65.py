"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    unown_bench_condition,
    unown_e_hidden_power,
    unown_equip,
)

card = PokemonCardDef(guid='9b46a198-65a5-59e3-862b-14907056269d', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownE.Name', display_name='Unown [E]', searchable_by=['Unown [E]', 'Basic', 'UnownE'], subtypes=['Basic'], collector_number=65, set_code='DP2', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='EQUIP', game_text='Once during your turn (before your attack), if Unown E is on your Bench, you may discard all cards attached to Unown E and attach Unown E to 1 of your Pokémon as a Pokémon Tool card. As long as Unown E is attached to a Pokémon, that Pokémon gets +10 HP.', ability_type=AbilityTypes.POKE_POWER, effect=unown_equip(), activation=Activations.ONCE_PER_TURN, condition=unown_bench_condition), Attack(title='Hidden Power', game_text="During your opponent's next turn, whenever your opponent flips a coin, treat it as tails.", cost={PokemonTypes.COLORLESS: 2}, effect=unown_e_hidden_power())])
