"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_lickilicky_12_boundless_power,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='0fbc1354-3338-5540-ba7e-920e593c4b99', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name', display_name='Lickilicky', searchable_by=['Lickilicky', 'Stage 1', 'Lickilicky'], subtypes=['Stage 1'], collector_number=12, set_code='DP3', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name', family_id=108, abilities=[Attack(title='Tongue Reel', game_text="Choose 1 of your opponent's Pokémon. If you choose a Benched Pokémon, switch the Defending Pokémon with that Pokémon. This attack does 20 damage to the Pokémon you chose. Flip a coin. If heads, the Defending Pokémon is now Paralyzed.", cost={PokemonTypes.COLORLESS: 2}, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Boundless Power', game_text="During your next turn, Lickilicky can't attack.", cost={PokemonTypes.COLORLESS: 4}, damage=80, effect=dp3_lickilicky_12_boundless_power())])
