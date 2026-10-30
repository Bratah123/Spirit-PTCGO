"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    gather_up_energy,
    marvelous_shine_counters,
)

card = PokemonCardDef(guid='a0b2bdbc-6794-59d2-b9ca-bee34d885904', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name', display_name='Gabite', searchable_by=['Gabite', 'Stage 1', 'Gabite'], subtypes=['Stage 1'], collector_number=48, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.COLORLESS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name', family_id=443, abilities=[Attack(title='Gather Up', game_text='Search your discard pile for up to 2 Energy cards, show them to your opponent, and put them into your hand.', cost={PokemonTypes.COLORLESS: 1}, effect=gather_up_energy(2)), Attack(title='Marvelous Shine', game_text="Flip a coin. If heads put 4 damage counters on 1 of your opponent's Pokémon. If tails, remove 4 damage counters from 1 of your Pokémon.", cost={PokemonTypes.COLORLESS: 2}, effect=marvelous_shine_counters())])
