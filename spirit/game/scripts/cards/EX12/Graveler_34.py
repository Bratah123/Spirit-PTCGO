"""STUB: effect not implemented — do not guess mechanics.
Graveler (EX12 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import (
    exoskeleton_passive,
)

card = PokemonCardDef(guid='da5cea20-3743-58c8-bb6e-e8bb34fe458c', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name', display_name='Graveler', searchable_by=['Graveler', 'Stage 1', 'Graveler'], subtypes=['Stage 1'], collector_number=34, set_code='EX12', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name', family_id=74, abilities=[Ability(title='Exoskeleton', game_text='Any damage done to Graveler by attacks is reduced by 10 (after applying Weakness and Resistance).', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=exoskeleton_passive(10)), Attack(title='Rock Slide', game_text="Does 10 damage to 2 of your opponent's Benched Pokémon (1 if there is only 1). (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=snipe_attack(10, pool='bench', count=2, also_base=True))])
