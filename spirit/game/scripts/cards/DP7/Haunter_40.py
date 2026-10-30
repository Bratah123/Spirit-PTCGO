"""STUB: effect not implemented — do not guess mechanics.
Haunter (DP7 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp7_haunter_40_hoodwink,
)

card = PokemonCardDef(guid='a5063520-286d-5820-9fa3-f309bb3f09c2', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name', display_name='Haunter', searchable_by=['Haunter', 'Stage 1', 'Haunter'], subtypes=['Stage 1'], collector_number=40, set_code='DP7', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name', family_id=92, abilities=[Attack(title='Smog', game_text='The Defending Pokémon is now Poisoned.', cost={}, effect=condition_attack(SpecialConditions.POISONED)), Attack(title='Hoodwink', game_text="You may search your opponent's discard pile for up to 3 in any combination of Trainer, Supporter, or Stadium cards and put them into your opponent's hand.", cost={PokemonTypes.PSYCHIC: 1}, damage=30, effect=dp7_haunter_40_hoodwink())])
