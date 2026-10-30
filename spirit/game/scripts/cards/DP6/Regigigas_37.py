"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_regigigas_37_recover_mechanism,
)
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(guid='ae2ab9b6-fb0c-53cb-94d8-c5d6f5a6dfe3', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name', display_name='Regigigas', searchable_by=['Regigigas', 'Basic', 'Regigigas'], subtypes=['Basic'], collector_number=37, set_code='DP6', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, family_id=486, abilities=[Ability(title='Recover Mechanism', game_text='When you attach an Energy card from your hand to Regigigas, remove all Special Conditions from Regigigas.', ability_type=AbilityTypes.POKE_BODY, effect=dp6_regigigas_37_recover_mechanism(), activation=Activations.ONCE_PER_TURN), Attack(title='Gigaton Punch', game_text="Flip a coin. If heads, this attack does 60 damage plus 20 more damage and does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 3}, damage=60, damage_operator='+', effect=flip_bonus(20))])
