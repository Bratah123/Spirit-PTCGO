"""STUB: effect not implemented — do not guess mechanics.
Lunatone (EX12 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    moon_guidance_trainer,
    sol_shade_passive,
)

card = PokemonCardDef(guid='ea2e76c8-941c-596d-9a88-d8162f18f424', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name', display_name='Lunatone', searchable_by=['Lunatone', 'Basic', 'Lunatone'], subtypes=['Basic'], collector_number=20, set_code='EX12', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=337, abilities=[Ability(title='Sol Shade', game_text="As long as you have Solrock in play, each player's Fire Pokémon (excluding Pokémon-ex) can't use any Poké-Powers.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=sol_shade_passive()), Attack(title='Moon Guidance', game_text='Search your deck for a Trainer card (excluding Supporter cards), show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=moon_guidance_trainer()), Attack(title='Psyshock', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.PSYCHIC: 1}, damage=10, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
