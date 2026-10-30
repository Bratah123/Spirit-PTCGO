"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_kirlia_53_psychic_research,
    dp3_kirlia_53_telekinesis,
)

card = PokemonCardDef(guid='de3c96ca-00c7-5d88-a901-8048ef652dc3', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name', display_name='Kirlia', searchable_by=['Kirlia', 'Stage 1', 'Kirlia'], subtypes=['Stage 1'], collector_number=53, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name', family_id=280, abilities=[Attack(title='Psychic Research', game_text='Search your discard pile for a Supporter card and use the effect of that card as the effect of this attack. (The Supporter card remains in your discard pile.)', cost={PokemonTypes.PSYCHIC: 1}, effect=dp3_kirlia_53_psychic_research()), Attack(title='Telekinesis', game_text="Choose 1 of your opponent's Pokémon. This attack does 40 damage to that Pokémon. This attack's damage isn't affected by Weakness or Resistance.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, effect=dp3_kirlia_53_telekinesis())])
