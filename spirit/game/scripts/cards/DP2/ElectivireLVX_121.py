"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    pulse_barrier,
    shocking_tail_passive,
)

card = PokemonCardDef(guid='f7d6ef22-5c2b-5bce-b043-f39430ad9774', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.ElectivireLVX.Name', display_name='Electivire LV.X', searchable_by=['Electivire LV.X', 'Level-Up', 'ElectivireLVX'], subtypes=['Level-Up'], collector_number=121, set_code='DP2', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.LEVELUP, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name', family_id=466, abilities=[Ability(title='Shocking Tail', game_text='As long as Electivire is your Active Pokémon, whenever your opponent attaches an Energy card from his or her hand to 1 of his or her Pokémon, put 2 damage counters on that Pokémon.', ability_type=AbilityTypes.POKE_BODY, passive=shocking_tail_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Pulse Barrier', game_text="Discard all of your opponent's Pokémon Tool cards and Stadium cards in play. If you do, prevent all effects, including damage, done to Electivire during your opponent's next turn.", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=pulse_barrier(50))])
