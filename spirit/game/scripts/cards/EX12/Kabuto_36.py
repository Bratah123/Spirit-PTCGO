"""STUB: effect not implemented — do not guess mechanics.
Kabuto (EX12 #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    ancient_protection_passive,
    granite_head,
)

card = PokemonCardDef(guid='a3e5d6fb-2887-51e2-ad60-eea9aa201aa7', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name', display_name='Kabuto', searchable_by=['Kabuto', 'Stage 1', 'Kabuto'], subtypes=['Stage 1'], collector_number=36, set_code='EX12', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name', family_id=140, abilities=[Ability(title='Ancient Protection', game_text='Each of your Omanyte, Omastar, Kabuto, Kabutops, and Kabutops ex has no Weakness.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=ancient_protection_passive('Omanyte', 'Omastar', 'Kabuto', 'Kabutops')), Attack(title='Granite Head', game_text="During your opponent's next turn, any damage done to Kabuto by attacks is reduced by 10 (after applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=granite_head(10))])
