"""STUB: effect not implemented — do not guess mechanics.
Magnezone (DPP #DP44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dpp_magnezone_dp44_charge_beam,
    dpp_magnezone_dp44_metallic_bolt,
)

card = PokemonCardDef(guid='ad504541-fa8a-51a5-8cbc-645fb06fa257', key='DPP', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name', display_name='Magnezone', searchable_by=['Magnezone', 'Stage 2', 'Magnezone'], subtypes=['Stage 2'], collector_number=44, set_code='DPP', rarity=Rarities.RarePromo, hp=130, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name', family_id=462, abilities=[Attack(title='Charge Beam', game_text='Search your discard pile for an Energy card and attach it to Magnezone.', cost={PokemonTypes.LIGHTNING: 1}, damage=30, effect=dpp_magnezone_dp44_charge_beam()), Attack(title='Metallic Bolt', game_text="You may discard a Lightning Energy and a Metal Energy attached to Magnezone. If you do, this attack's base damage is 120 instead of 60.", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dpp_magnezone_dp44_metallic_bolt())])
