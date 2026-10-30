"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    delta_block_powers_passive,
    mind_play_discard_hand_card,
)

card = PokemonCardDef(guid='c74ecadf-2ab1-5ee5-ad13-9529ea4a5e58', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name', display_name='Golduck δ', searchable_by=['Golduck δ', 'Stage 1', 'Golduck'], subtypes=['Stage 1'], collector_number=43, set_code='EX13', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name', family_id=55, abilities=[Ability(title='Delta Block', game_text="As long as any Stadium card with Holon in its name is in play, your opponent can't play any Stadium cards from his or her hand.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=delta_block_powers_passive()), Attack(title='Mind Play', game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose. If that card is a Trainer card, this attack does 30 damage plus 30 more damage, and discard that card. If that card is not a Trainer card, return it to your opponent's hand.", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=mind_play_discard_hand_card())])
