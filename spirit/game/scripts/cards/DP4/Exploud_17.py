"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_exploud_17_ambient_noise,
)

card = PokemonCardDef(guid='ae10e401-6a28-526e-a22c-71dee4f81aec', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name', display_name='Exploud', searchable_by=['Exploud', 'Stage 2', 'Exploud'], subtypes=['Stage 2'], collector_number=17, set_code='DP4', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name', family_id=293, abilities=[Attack(title='Ambient Noise', game_text="Flip 2 coins. If the first coin is heads, this attack does 50 damage to the Defending Pokémon. If the first coin is tails, this attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) If the second coin is heads, the Defending Pokémon is now Confused. If the second coin is tails, your opponent can't play any Trainer, Supporter, or Stadium cards from his or her hand during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, effect=dp4_exploud_17_ambient_noise()), Attack(title='Hyper Voice', cost={PokemonTypes.COLORLESS: 4}, damage=70)])
