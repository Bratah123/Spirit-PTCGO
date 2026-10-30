"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_hariyama_41_palm_strike,
    dp4_hariyama_41_spirited_throw,
)

card = PokemonCardDef(guid='b659a97b-9a33-55fd-b05c-b98ae01c310d', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name', display_name='Hariyama', searchable_by=['Hariyama', 'Stage 1', 'Hariyama'], subtypes=['Stage 1'], collector_number=41, set_code='DP4', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name', family_id=296, abilities=[Attack(title='Palm Strike', game_text='Flip a coin. If heads, this attack does 20 damage plus 40 more damage.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp4_hariyama_41_palm_strike()), Attack(title='Spirited Throw', game_text="If Hariyama has fewer remaining HP than the Defending Pokémon, this attack's base damage is 80.", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=dp4_hariyama_41_spirited_throw())])
