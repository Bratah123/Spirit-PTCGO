"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    give_aid,
    mother_pheromone_passive,
)

card = PokemonCardDef(guid='4096a51d-fa8a-55f1-932c-414290b2adb1', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name', display_name='Nidoqueen', searchable_by=['Nidoqueen', 'Stage 2', 'Nidoqueen'], subtypes=['Stage 2'], collector_number=31, set_code='DP2', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name', family_id=29, abilities=[Ability(title='Mother Pheromone', game_text="The attack cost of your Nidoran ♀, Nidorina, Nidoran ♂, Nidorino, and Nidoking's attacks is Colorless less.", ability_type=AbilityTypes.POKE_BODY, passive=mother_pheromone_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Give Aid', game_text="If you have the same number of or less Benched Pokémon than your opponent, this attack's base damage is 50 instead of 90.", cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=90, effect=give_aid(90))])
