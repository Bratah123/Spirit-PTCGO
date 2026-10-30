"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    poison_spike,
    spike_armor_reflect,
)

card = PokemonCardDef(guid='f0871bb0-e59e-5321-a829-d5d2c1c633e5', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name', display_name='Sandslash', searchable_by=['Sandslash', 'Stage 1', 'Sandslash'], subtypes=['Stage 1'], collector_number=61, set_code='DP2', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name', family_id=27, abilities=[Attack(title='Spike Armor', game_text="During your opponent's next turn, if Sandslash is damaged by an opponent's attack (even if Sandslash is Knocked Out), put 4 damage counters on the Attacking Pokémon.", cost={PokemonTypes.COLORLESS: 1}, effect=spike_armor_reflect()), Attack(title='Poison Spike', game_text='If the Defending Pokémon already has any damage counters on it, that Pokémon is now Poisoned.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=poison_spike(60))])
