"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_jynx_30_lovely_kiss,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='72bbdb08-60aa-5f68-be21-a147ff9bd26b', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name', display_name='Jynx', searchable_by=['Jynx', 'Basic', 'Jynx'], subtypes=['Basic'], collector_number=30, set_code='DP3', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=124, abilities=[Attack(title='Icy Kiss', game_text="If Jynx was damaged by an attack during your opponent's last turn, the Defending Pokémon is now Paralyzed.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.PARALYZED)), Attack(title='Lovely Kiss', game_text='Move 2 damage counters from Jynx to the Defending Pokémon. If Smoochum is anywhere under Jynx, move 4 damage counters instead.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, effect=dp3_jynx_30_lovely_kiss())])
