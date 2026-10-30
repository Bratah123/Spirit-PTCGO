"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    extend_fungus,
    wild_spores,
)

card = PokemonCardDef(guid='47d35c40-733c-592e-9d1a-1f4f8a4b0778', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name', display_name='Parasect', searchable_by=['Parasect', 'Stage 1', 'Parasect'], subtypes=['Stage 1'], collector_number=58, set_code='DP2', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name', family_id=46, abilities=[Attack(title='Wild Spores', game_text='If Parasect evolved from Paras during this turn, this attack does 40 damage and the Defending Pokémon is now Asleep and Poisoned.', cost={PokemonTypes.GRASS: 1}, damage=20, effect=wild_spores()), Attack(title='Extend Fungus', game_text='Remove 2 damage counters from Parasect.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=extend_fungus(60))])
