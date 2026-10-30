"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_froslass_3_icy_breath,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(guid='d0aaf05b-c68f-517d-aa73-8a5d1ab760a9', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name', display_name='Froslass', searchable_by=['Froslass', 'Stage 1', 'Froslass'], subtypes=['Stage 1'], collector_number=3, set_code='DP6', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name', family_id=478, abilities=[Attack(title='Destiny Bond', game_text="Discard a Psychic Energy attached to Froslass. During your opponent's next turn, if Froslass would be Knocked Out by damage from an attack, the Attacking Pokémon is Knocked Out.", cost={PokemonTypes.PSYCHIC: 1}, effect=self_energy_discard_attack(count=1, then_damage=0)), Attack(title='Icy Breath', game_text="The Defending Pokémon is now Asleep. Put 1 damage counter on each of your opponent's Benched Pokémon.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp6_froslass_3_icy_breath())])
