"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    evolutionary_toxic_on_evolve,
    strike_and_fade_snipe,
)

card = PokemonCardDef(guid='edb5a67e-62b5-5b21-ace1-28823e2c7173', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name', display_name='Crobat', searchable_by=['Crobat', 'Stage 2', 'Crobat'], subtypes=['Stage 2'], collector_number=23, set_code='DP2', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name', family_id=41, abilities=[Ability(title='Evolutionary Toxic', game_text='Once during your turn, when you play Crobat from your hand to evolve 1 of your Pokémon, you may choose 1 of the Defending Pokémon. That Pokémon is now Poisoned. Put 2 damage counters instead of 1 on that Pokémon between turns.', ability_type=AbilityTypes.POKE_POWER, effect=evolutionary_toxic_on_evolve(), trigger=Triggers.ON_EVOLVE), Attack(title='Strike and Fade', game_text="Choose 1 of your opponent's Pokémon. This attack does 50 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Flip a coin. If tails, shuffle Crobat and all cards attached to it back into your deck.", cost={PokemonTypes.PSYCHIC: 2}, effect=strike_and_fade_snipe(30))])
