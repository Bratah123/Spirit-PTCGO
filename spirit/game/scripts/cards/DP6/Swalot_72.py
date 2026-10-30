"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_swalot_72_swallow_up,
)

card = PokemonCardDef(guid='8652a85b-ca6c-5628-baca-1f7cf47f0f13', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name', display_name='Swalot', searchable_by=['Swalot', 'Stage 1', 'Swalot'], subtypes=['Stage 1'], collector_number=72, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name', family_id=316, abilities=[Attack(title='Swallow Up', game_text="Before doing damage, count the remaining HP of the Defending Pokémon and Swalot. If the Defending Pokémon has fewer remaining HP than Swalot's, this attack does 80 damage instead.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=dp6_swalot_72_swallow_up()), Attack(title='Gunk Shot', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=condition_attack(SpecialConditions.POISONED))])
