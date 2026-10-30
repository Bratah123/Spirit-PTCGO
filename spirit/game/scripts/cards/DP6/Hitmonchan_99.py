"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_hitmonchan_99_counter_punch,
    dp6_hitmonchan_99_gut_strike,
)

card = PokemonCardDef(guid='0d2f8dee-d8fb-5a5d-b9c7-479458d9ad63', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name', display_name='Hitmonchan', searchable_by=['Hitmonchan', 'Basic', 'Hitmonchan'], subtypes=['Basic'], collector_number=99, set_code='DP6', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=107, abilities=[Attack(title='Counter Punch', game_text="During your opponent's next turn, if Hitmonchan is damaged by an opponent's attack (even if Hitmonchan is Knocked Out), put 4 damage counters on the Attacking Pokémon.", cost={PokemonTypes.FIGHTING: 1}, effect=dp6_hitmonchan_99_counter_punch()), Attack(title='Gut Strike', game_text="If Tyrogue is anywhere under Hitmonchan, this attack's base damage is 60 instead of 30.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=dp6_hitmonchan_99_gut_strike())])
