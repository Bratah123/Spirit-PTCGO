"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.dp import (
    electro_recycle,
    electro_recycle_condition,
)

card = PokemonCardDef(guid='d617dcaa-8d91-542b-a41a-6a2a93ff1006', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name', display_name='Pikachu', searchable_by=['Pikachu', 'Basic', 'Pikachu'], subtypes=['Basic'], collector_number=16, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=25, abilities=[Ability(title='Electro Recycle', game_text="Once during your turn (before your attack), if Pichu is anywhere under Pikachu, you may search your discard pile for a Lightning Energy card, show it to your opponent, and put it into your hand. This power can't be used if Pikachu is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=electro_recycle(), activation=Activations.ONCE_PER_TURN, condition=electro_recycle_condition), Attack(title='BikaBika', game_text='Flip a coin. If heads, this attack does 20 damage plus 10 more damage.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=flip_bonus(10))])
