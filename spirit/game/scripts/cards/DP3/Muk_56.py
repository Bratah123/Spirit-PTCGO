"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_muk_56_panic_liquid,
    dp3_muk_56_toxic_sludge,
)

card = PokemonCardDef(guid='066c0cd9-5b9f-529b-8fa8-536c6ca17a3d', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name', display_name='Muk', searchable_by=['Muk', 'Stage 1', 'Muk'], subtypes=['Stage 1'], collector_number=56, set_code='DP3', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name', family_id=88, abilities=[Ability(title='Toxic Sludge', game_text="At the end of each player's turn, each of your opponent's Active Pokémon that has any Grass Energy attached to it is now Poisoned. If that Pokémon is already Poisoned, Toxic Sludge Poké-Body does nothing to that Pokémon.", ability_type=AbilityTypes.POKE_BODY, effect=dp3_muk_56_toxic_sludge(), activation=Activations.ONCE_PER_TURN), Attack(title='Panic Liquid', game_text="The Defending Pokémon is now Confused and can't retreat during your opponent's next turn.", cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=dp3_muk_56_panic_liquid())])
