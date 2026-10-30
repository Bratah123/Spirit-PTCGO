"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp5_umbreon_32_moonlight_veil,
)

card = PokemonCardDef(guid='a7ef71f0-52c1-5ed2-98ac-e74c102c8495', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name', display_name='Umbreon', searchable_by=['Umbreon', 'Stage 1', 'Umbreon'], subtypes=['Stage 1'], collector_number=32, set_code='DP5', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name', family_id=133, abilities=[Ability(title='Moonlight Veil', game_text="Each of your Pokémon that evolves from Eevee has no Weakness, and that Pokémon's Retreat Cost is 0.", ability_type=AbilityTypes.POKE_BODY, passive=dp5_umbreon_32_moonlight_veil(), activation=Activations.ONCE_PER_TURN), Attack(title='Confuse Ray', game_text='The Defending Pokémon is now Confused.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=condition_attack(SpecialConditions.CONFUSED))])
