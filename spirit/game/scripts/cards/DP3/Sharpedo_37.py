"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_sharpedo_37_rough_skin,
    dp3_sharpedo_37_strike_wound,
)

card = PokemonCardDef(guid='829cd0e1-5020-553c-8a1f-34cc1df1bf0c', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name', display_name='Sharpedo', searchable_by=['Sharpedo', 'Stage 1', 'Sharpedo'], subtypes=['Stage 1'], collector_number=37, set_code='DP3', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name', family_id=318, abilities=[Ability(title='Rough Skin', game_text="If Sharpedo is your Active Pokémon and is damaged by an opponent's attack (even if Sharpedo is Knocked Out), put 2 damage counters on the Attacking Pokémon.", ability_type=AbilityTypes.POKE_BODY, effect=dp3_sharpedo_37_rough_skin(), activation=Activations.ONCE_PER_TURN), Attack(title='Strike Wound', game_text="If the Defending Pokémon has 2 or more damage counters on it, this attack does 60 damage plus 20 more damage. This attack damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp3_sharpedo_37_strike_wound())])
