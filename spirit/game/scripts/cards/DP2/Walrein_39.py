"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    freeze_up_on_evolve,
    ice_bind,
)

card = PokemonCardDef(guid='1daa11fe-2769-583c-8642-2350655a2de5', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name', display_name='Walrein', searchable_by=['Walrein', 'Stage 2', 'Walrein'], subtypes=['Stage 2'], collector_number=39, set_code='DP2', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name', family_id=363, abilities=[Ability(title='Freeze-up', game_text="Once during your turn, when you play Walrein from your hand to evolve 1 of your Pokémon, you may flip 2 coins. If both are heads, discard 1 of the Defending Pokémon and all cards attached to it. (This doesn't count as a Knocked Out Pokémon.)", ability_type=AbilityTypes.POKE_POWER, effect=freeze_up_on_evolve(), trigger=Triggers.ON_EVOLVE), Attack(title='Ice Bind', game_text="If your opponent doesn't discard a card from his or her hand, the Defending Pokémon is now Paralyzed.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=70, effect=ice_bind(70))])
