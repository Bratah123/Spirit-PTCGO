"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    memory_out_passive,
)
from spirit.game.card_effects.attacks_common import bonus_if, named_in_play

card = PokemonCardDef(guid='a03f6da9-fb05-5d36-aabb-3e98a005439c', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name', display_name='Uxie', searchable_by=['Uxie', 'Basic', 'Uxie'], subtypes=['Basic'], collector_number=18, set_code='DP2', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=480, abilities=[Ability(title='Memory Out', game_text="Once during your opponent's turn, if Uxie is damaged by an opponent's attack (even if Uxie is Knocked Out), you may use this power. The Attacking Pokémon can't use that attack during your opponent's next turn.", ability_type=AbilityTypes.POKE_POWER, passive=memory_out_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Mind Off', game_text='If you have Mesprit and Azelf in play, this attack does 10 damage plus 20 more damage and the Defending Pokémon is now Asleep.', cost={PokemonTypes.PSYCHIC: 1}, damage=10, damage_operator='+', effect=bonus_if(named_in_play('Mesprit', 'Azelf', require_all=True), 20, base=10))])
