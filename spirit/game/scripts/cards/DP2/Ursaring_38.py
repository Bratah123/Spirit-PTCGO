"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    bad_temper,
)
from spirit.game.card_effects.attacks_common import bonus_if, named_in_play

card = PokemonCardDef(guid='118015fa-4531-5e2f-81a7-f98a5719f231', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name', display_name='Ursaring', searchable_by=['Ursaring', 'Stage 1', 'Ursaring'], subtypes=['Stage 1'], collector_number=38, set_code='DP2', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name', family_id=216, abilities=[Attack(title='Bad Temper', game_text="The Defending Pokémon is now Confused. During your opponent's next turn, that Pokémon's attacks do 60 more damage to the Active Pokémon (before applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=bad_temper()), Attack(title='Defensive Claw', game_text='If Teddiursa is on your Bench, this attack does 60 damage plus 20 more damage. If Teddiursa is on your Bench and has any damage counters on it, this attack does 60 damage plus 40 more damage and remove all damage counters from that Pokémon.', cost={PokemonTypes.COLORLESS: 4}, damage=60, damage_operator='+', effect=bonus_if(named_in_play('Teddiursa'), 20, base=60))])
