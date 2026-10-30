"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import knock_off_random_hand
from spirit.game.card_effects.dp import (
    energy_cyclone,
)

card = PokemonCardDef(guid='3ad57890-7f01-5ff9-b47f-be5a19d5b72a', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name', display_name='Feraligatr', searchable_by=['Feraligatr', 'Stage 2', 'Feraligatr'], subtypes=['Stage 2'], collector_number=8, set_code='DP2', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name', family_id=158, abilities=[Attack(title='Energy Cyclone', game_text='Choose as many Energy cards from your hand as you like and show them to your opponent. This attack does 20 damage times the number of Energy cards you chose. Put those Energy cards on top of your deck. Shuffle your deck afterward.', cost={PokemonTypes.WATER: 2}, damage=20, damage_operator='x', effect=energy_cyclone(20)), Attack(title='Breaking Tail', game_text="Choose 1 card from your opponent's hand without looking and discard it.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=knock_off_random_hand())])
