"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    ground_burn,
    payback,
)

card = PokemonCardDef(guid='1f973bb5-c5ca-56db-a0cf-803ec747ca94', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name', display_name='Tyranitar', searchable_by=['Tyranitar', 'Stage 2', 'Tyranitar'], subtypes=['Stage 2'], collector_number=17, set_code='DP2', rarity=Rarities.RareHolo, hp=140, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name', family_id=246, abilities=[Attack(title='Payback', game_text="If your opponent has only 1 Prize card left, this attack does 40 damage plus 40 more damage and discard the top 3 cards from your opponent's deck.", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=payback(40, 40, mill=3)), Attack(title='Ground Burn', game_text='Each player discards the top card of his or her deck. This attack does 80 damage plus 20 more damage for each Energy card discarded in this way.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.DARKNESS: 2}, damage=80, damage_operator='+', effect=ground_burn(80, 20))])
