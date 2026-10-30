"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    delta_reserve_passive,
    rotating_claws,
)

card = PokemonCardDef(guid='84fb6292-fb3f-5132-b7c5-62e85ea4985c', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name', display_name='Pidgeot δ', searchable_by=['Pidgeot δ', 'Stage 2', 'Pidgeot'], subtypes=['Stage 2'], collector_number=14, set_code='EX13', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name', family_id=18, abilities=[Ability(title='Delta Reserve', game_text="As long as Pidgeot has any Holon Energy cards attached to it, each player's Pokémon (excluding Pokémon that has δ on its card) can't use any Poké-Powers.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=delta_reserve_passive()), Attack(title='Rotating Claws', game_text='You may discard an Energy card attached to Pidgeot. If you do, search your discard pile for an Energy card (excluding the one you discarded) and attach it to Pidgeot.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=rotating_claws())])
