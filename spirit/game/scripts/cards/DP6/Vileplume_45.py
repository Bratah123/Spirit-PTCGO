"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_vileplume_45_disturbing_pollen,
    dp6_vileplume_45_energy_reaction,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='4661bca6-364d-579d-8c3b-108dea4f541a', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name', display_name='Vileplume', searchable_by=['Vileplume', 'Stage 2', 'Vileplume'], subtypes=['Stage 2'], collector_number=45, set_code='DP6', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name', family_id=43, abilities=[Ability(title='Energy Reaction', game_text="Once during your turn (before your attack), when you attach a Grass or Psychic Energy card from your hand to Vileplume (excluding effects of attacks or Poké-Powers), you may use this power. If you attach a Grass Energy card, the Defending Pokémon is now Asleep. If you attach a Psychic Energy card, the Defending Pokémon is now Poisoned. This power can't be used if Vileplume is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_vileplume_45_energy_reaction(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Disturbing Pollen', game_text="Flip a coin. If heads, your opponent can't play any Trainer, Supporter, or Stadium cards from his or her hand during your opponent's next turn.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp6_vileplume_45_disturbing_pollen())])
