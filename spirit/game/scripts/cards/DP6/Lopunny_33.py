"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.dp import (
    dp6_lopunny_33_cross_cut,
    dp6_lopunny_33_healing_tail_passive,
)

card = PokemonCardDef(guid='b8d78a4f-ffd7-5c96-b28a-d78546a83d2c', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name', display_name='Lopunny', searchable_by=['Lopunny', 'Stage 1', 'Lopunny'], subtypes=['Stage 1'], collector_number=33, set_code='DP6', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name', family_id=427, abilities=[Ability(title='Healing Tail', game_text='As long as Lopunny is your Active Pokémon, remove 1 damage counter from each of your Benched Pokémon between turns.', ability_type=AbilityTypes.POKE_BODY, passive=dp6_lopunny_33_healing_tail_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Collect', game_text='Draw 3 cards.', cost={}, effect=draw_attack(3)), Attack(title='Cross-Cut', game_text='If the Defending Pokémon is an Evolved Pokémon, this attack does 30 damage plus 30 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=dp6_lopunny_33_cross_cut())])
