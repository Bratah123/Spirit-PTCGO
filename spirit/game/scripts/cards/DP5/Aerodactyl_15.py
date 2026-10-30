"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp5_aerodactyl_15_primal_claw_passive,
)

card = PokemonCardDef(guid='79d1e7d5-5b43-5a62-a3ec-3c82afbdd763', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name', display_name='Aerodactyl', searchable_by=['Aerodactyl', 'Stage 1', 'Aerodactyl'], subtypes=['Stage 1'], collector_number=15, set_code='DP5', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.OldAmber.Name', family_id=142, abilities=[Ability(title='Primal Claw', game_text="After your opponent's Pokémon uses a Poké-Power, put 2 damage counters on that Pokémon.", ability_type=AbilityTypes.POKE_BODY, passive=dp5_aerodactyl_15_primal_claw_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Supersonic', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.', cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=condition_attack(SpecialConditions.CONFUSED, flip=True))])
