"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_ditto_27_ditto_dna_passive,
)

card = PokemonCardDef(guid='2b597b57-a05e-5aca-8b16-59935de8a509', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name', display_name='Ditto', searchable_by=['Ditto', 'Basic', 'Ditto'], subtypes=['Basic'], collector_number=27, set_code='DP6', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=132, abilities=[Ability(title='Ditto DNA', game_text="As long as Ditto is your Active Pokémon, its maximum HP is the same as your opponent's Active Pokémon. Ditto can use the attacks of that Pokémon as its own. (You still need the necessary Energy to use each attack.) If that Pokémon is no longer your opponent's Active Pokémon, choose 1 of your opponent's Active Pokémon for Ditto to copy.", ability_type=AbilityTypes.POKE_BODY, passive=dp6_ditto_27_ditto_dna_passive(), activation=Activations.ONCE_PER_TURN)])
