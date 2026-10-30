"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    power_cancel_passive,
    psychic_guard,
)

card = PokemonCardDef(guid='f6924df9-3e53-5e83-b057-3b944f0afd9a', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name', display_name='Alakazam', searchable_by=['Alakazam', 'Stage 2', 'Alakazam'], subtypes=['Stage 2'], collector_number=2, set_code='DP2', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name', family_id=65, abilities=[Ability(title='Power Cancel', game_text="Once during your opponent's turn, when your opponent's Pokémon uses any Poké-Power, you may discard 2 cards from your hand and prevent all effects of that Poké-Power. (This counts as that Pokémon using its Poké-Power.) This power can't be used if Alakazam is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, passive=power_cancel_passive()), Attack(title='Psychic Guard', game_text="During your opponent's next turn, any damage done to Alakazam by attacks from your opponent's Stage 2 Evolved Pokémon is reduced by 30 (after applying Weakness and Resistance).", cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=psychic_guard(50, 20))])
