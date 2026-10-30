"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    heal_attack,
)

card = PokemonCardDef(guid='559da89e-8e90-562c-8293-7ed4177e2dd0', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name', display_name='Ivysaur', searchable_by=['Ivysaur', 'Stage 1', 'Ivysaur'], subtypes=['Stage 1'], collector_number=51, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name', family_id=1, abilities=[Attack(title='Leech Seed', game_text='Remove 1 damage counter from Ivysaur.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=heal_attack(10)), Attack(title='Razor Leaf', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1}, damage=60)])
