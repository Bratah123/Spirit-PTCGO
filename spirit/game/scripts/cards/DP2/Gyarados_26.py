"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dragon_dna_passive,
    enrage_low_hp,
)

card = PokemonCardDef(guid='0a106539-7928-50b0-9637-6940d74b7dac', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name', display_name='Gyarados', searchable_by=['Gyarados', 'Stage 1', 'Gyarados'], subtypes=['Stage 1'], collector_number=26, set_code='DP2', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name', family_id=129, abilities=[Ability(title='Dragon DNA', game_text="Gyarados can use any attack from its Basic Pokémon. (You still have to pay for that attack's Energy cost.) If Gyarados uses any attack from its Basic Pokémon, that attack does 30 more damage to the Defending Pokémon (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, passive=dragon_dna_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Enrage', game_text="Flip a coin until you get tails. For each heads, choose 1 card from your opponent's hand without looking and discard it. If the first coin is tails, Gyarados is now Confused.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2}, damage=80, effect=enrage_low_hp(80, 60))])
