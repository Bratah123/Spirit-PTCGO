"""STUB: effect not implemented — do not guess mechanics.
Dusknoir LV.X (DP7 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_dusknoirlvx_96_ectoplasm,
)

card = PokemonCardDef(guid='c92105b7-27b9-5216-b735-54dc9e3f926e', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.DusknoirLVX.Name', display_name='Dusknoir LV.X', searchable_by=['Dusknoir LV.X', 'Level-Up', 'DusknoirLVX'], subtypes=['Level-Up'], collector_number=96, set_code='DP7', rarity=Rarities.RareHolo, hp=140, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.LEVELUP, retreat_cost=3, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name', family_id=355, abilities=[Ability(title='Ectoplasm', game_text="If Dusknoir is your Active Pokémon and would be Knocked Out by damage from your opponent's attack, you may discard all cards attached to Dusknoir LV.X and put Dusknoir LV.X as a Stadium card into play instead of discarding it. This counts as Dusknoir being Knocked Out and your opponent takes a Prize card. As long as you have Dusknoir LV.X as a Stadium card in play, put 1 damage counter on each of your opponent's Pokémon between turns. If another Stadium card comes into play or Dusknoir LV.X is discarded by the effects of any attacks, Poké-Powers, Poké-Bodies, Trainer, or Supporter cards, return Dusknoir LV.X to your hand.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_dusknoirlvx_96_ectoplasm(), activation=Activations.ONCE_PER_TURN)])
