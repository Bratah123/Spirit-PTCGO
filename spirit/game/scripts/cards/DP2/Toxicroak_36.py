"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    poison_sacs_passive,
)

card = PokemonCardDef(guid='985a7b94-fd57-5e2d-a787-9f29abc03d0a', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name', display_name='Toxicroak', searchable_by=['Toxicroak', 'Stage 1', 'Toxicroak'], subtypes=['Stage 1'], collector_number=36, set_code='DP2', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name', family_id=453, abilities=[Ability(title='Poison Sacs', game_text="Your opponent can't remove the Special Condition Poisoned by evolving or devolving his or her Poisoned Pokémon. (This also includes putting a Pokémon Level-Up card onto the Poisoned Pokémon.)", ability_type=AbilityTypes.POKE_BODY, passive=poison_sacs_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Knuckle Claws', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.POISONED))])
