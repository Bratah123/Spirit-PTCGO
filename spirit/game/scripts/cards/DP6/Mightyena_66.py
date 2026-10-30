"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_mightyena_66_bite_on,
    dp6_mightyena_66_harass,
)

card = PokemonCardDef(guid='a1a1fa7f-d0b4-54e8-8153-47dec52b59c0', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name', display_name='Mightyena', searchable_by=['Mightyena', 'Stage 1', 'Mightyena'], subtypes=['Stage 1'], collector_number=66, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name', family_id=261, abilities=[Attack(title='Bite On', game_text="If the Defending Pokémon isn't an Evolved Pokémon, that Pokémon can't attack, retreat, or use any Poké-Powers during your opponent's next turn.", cost={PokemonTypes.DARKNESS: 1}, damage=30, effect=dp6_mightyena_66_bite_on()), Attack(title='Harass', game_text='Does 10 damage times the number of Pokémon you have in play.', cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='x', effect=dp6_mightyena_66_harass())])
