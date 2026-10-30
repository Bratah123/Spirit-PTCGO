"""STUB: effect not implemented — do not guess mechanics.
Omastar (EX12 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    ancient_fang_passive,
    drag_off_optional,
)

card = PokemonCardDef(guid='61ce97aa-e665-583d-b2b8-5f46d00c2278', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name', display_name='Omastar', searchable_by=['Omastar', 'Stage 2', 'Omastar'], subtypes=['Stage 2'], collector_number=23, set_code='EX12', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name', family_id=138, abilities=[Ability(title='Ancient Fang', game_text="As long as you have Kabuto, Kabutops, or Kabutops ex in play, Omastar's attacks do 20 more damage to the Defending Pokémon (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=ancient_fang_passive('Kabuto', 'Kabutops', bonus=20)), Attack(title='Drag Off', game_text="Before doing damage, you may choose 1 of your opponent's Benched Pokémon and switch it with 1 of the Defending Pokémon. Your opponent chooses the Defending Pokémon to switch.", cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=drag_off_optional()), Attack(title='Hydro Splash', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=50)])
