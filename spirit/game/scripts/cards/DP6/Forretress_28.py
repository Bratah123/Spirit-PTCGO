"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_forretress_28_explosion,
    dp6_forretress_28_iron_shell,
)

card = PokemonCardDef(guid='53c33965-c3cf-5745-8174-3c3639585c87', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name', display_name='Forretress', searchable_by=['Forretress', 'Stage 1', 'Forretress'], subtypes=['Stage 1'], collector_number=28, set_code='DP6', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name', family_id=204, abilities=[Ability(title='Iron Shell', game_text="Whenever you attach a basic Energy card from your hand to Forretress (excluding effects of attacks), you may flip a coin. If tails, put 2 damage counters on each Pokémon (both yours and your opponent's) (excluding any Forretress).", ability_type=AbilityTypes.POKE_BODY, effect=dp6_forretress_28_iron_shell(), activation=Activations.ONCE_PER_TURN), Attack(title='Explosion', game_text='Forretress does 40 damage to itself.', cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2}, damage=100, effect=dp6_forretress_28_explosion())])
