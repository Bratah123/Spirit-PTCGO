"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import recover_from_discard

from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(guid='20a36390-3534-5d20-b808-b432abc05c13', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name', display_name='Nidorina', searchable_by=['Nidorina', 'Stage 1', 'Nidorina'], subtypes=['Stage 1'], collector_number=56, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name', family_id=29, abilities=[Attack(title='Rescue', game_text='Search your discard pile for up to 2 Pokémon, show them to your opponent, and put them into your hand.', cost={PokemonTypes.COLORLESS: 1}, effect=recover_from_discard(is_pokemon_card, count=1, minimum=0, reveal=True)), Attack(title='Scratch', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30)])
