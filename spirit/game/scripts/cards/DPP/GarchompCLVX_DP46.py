"""STUB: effect not implemented — do not guess mechanics.
Garchomp C LV.X (DPP #DP46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dpp_garchompclvx_dp46_healing_breath,
)
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='de23b221-dc44-5181-888d-f95dbfef1d36', key='DPP', name='com.direwolfdigital.cake.data.archetypes.pokemon.GarchompCLVX.Name', display_name='Garchomp C LV.X', searchable_by=['Garchomp C LV.X', 'Level-Up', 'SP', 'GarchompCLVX'], subtypes=['Level-Up', 'SP'], collector_number=46, set_code='DPP', rarity=Rarities.RarePromo, hp=110, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.LEVELUP, retreat_cost=0, weakness_type=PokemonTypes.COLORLESS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GarchompC.Name', family_id=445, abilities=[Ability(title='Healing Breath', game_text='Once during your turn (before your attack), when you put Garchomp C LV.X from your hand onto your Active Garchomp C, you may remove all damage counters from each of your Pokémon SP.', ability_type=AbilityTypes.POKE_POWER, effect=dpp_garchompclvx_dp46_healing_breath(), activation=Activations.ONCE_PER_TURN), Attack(title='Dragon Rush', game_text="Discard 2 Energy attached to Garchomp C. Choose 1 of your opponent's Pokémon. This attack does 80 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Garchomp C can't use Dragon Rush during your next turn.", cost={PokemonTypes.COLORLESS: 3}, effect=snipe_attack(80, pool='bench'))])
