"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.dp import (
    dp6_unownw_80_wall_passive,
)

card = PokemonCardDef(guid='e3fc7bef-603d-5b56-9008-e2277115ca9c', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownW.Name', display_name='Unown [W]', searchable_by=['Unown [W]', 'Basic', 'UnownW'], subtypes=['Basic'], collector_number=80, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='WALL', game_text="As long as Unown W is your Active Pokémon, any damage done to your Pokémon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, passive=dp6_unownw_80_wall_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Draw a card.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=draw_attack(1))])
