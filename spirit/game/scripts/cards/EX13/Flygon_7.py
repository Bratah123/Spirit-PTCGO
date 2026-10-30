"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import swift_attack
from spirit.game.card_effects.ex import (
    delta_supply_attach,
)

card = PokemonCardDef(guid='39e04ca3-2d7a-5bd7-99bd-18e05ead4213', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name', display_name='Flygon δ', searchable_by=['Flygon δ', 'Stage 2', 'Flygon'], subtypes=['Stage 2'], collector_number=7, set_code='EX13', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.GRASS, PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name', family_id=330, abilities=[Ability(title='Delta Supply', game_text="Once during your turn (before your attack), you may attach a basic Energy card or a δ Rainbow Energy card from your hand to 1 of your Pokémon that has δ on its card. This power can't be used if Flygon is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=delta_supply_attach(), activation=Activations.ONCE_PER_TURN), Attack(title='Swift', game_text="This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.", cost={PokemonTypes.GRASS: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=60, effect=swift_attack())])
