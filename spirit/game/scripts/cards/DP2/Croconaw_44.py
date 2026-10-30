"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import magma_ring_no_retreat
from spirit.game.card_effects.dp import (
    evolutionary_vitality_on_evolve,
)

card = PokemonCardDef(guid='050ce8e0-0375-5ee3-80c2-67daf8447962', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name', display_name='Croconaw', searchable_by=['Croconaw', 'Stage 1', 'Croconaw'], subtypes=['Stage 1'], collector_number=44, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name', family_id=158, abilities=[Ability(title='Evolutionary Vitality', game_text='Once during your turn, when you play Croconaw from your hand to evolve 1 of your Pokémon, you may look at the top 5 cards of your deck. Choose all Energy cards you find there, show them to your opponent, and put them into your hand. Put the other cards back on top of your deck. Shuffle your deck afterward.', ability_type=AbilityTypes.POKE_POWER, effect=evolutionary_vitality_on_evolve(), trigger=Triggers.ON_EVOLVE), Attack(title='Hover Over', game_text="The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=magma_ring_no_retreat())])
