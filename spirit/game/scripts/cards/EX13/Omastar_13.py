"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    vengeful_spikes,
)

card = PokemonCardDef(guid='b16b8eec-b3c5-5b19-9f5d-d03dfd080e73', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name', display_name='Omastar δ', searchable_by=['Omastar δ', 'Stage 2', 'Omastar'], subtypes=['Stage 2'], collector_number=13, set_code='EX13', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name', family_id=139, abilities=[Attack(title='Bind', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Vengeful Spikes', game_text="Does 30 damage plus 10 more damage for each Omanyte, Omastar, Kabuto, Kabutops, and Kabutops ex in your discard pile. You can't add more than 60 damage in this way.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=vengeful_spikes())])
