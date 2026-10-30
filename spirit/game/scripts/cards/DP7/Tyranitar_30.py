"""STUB: effect not implemented — do not guess mechanics.
Tyranitar (DP7 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.dp import (
    dp7_tyranitar_30_darkness_drive,
    dp7_tyranitar_30_grind,
)

card = PokemonCardDef(guid='16d9ada8-a333-5772-af8d-240541fd08ff', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name', display_name='Tyranitar', searchable_by=['Tyranitar', 'Stage 2', 'Tyranitar'], subtypes=['Stage 2'], collector_number=30, set_code='DP7', rarity=Rarities.Rare, hp=140, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name', family_id=246, abilities=[Ability(title='Darkness Drive', game_text="After your opponent's Pokémon uses a Poké-Power, you may search your discard pile for a basic Darkness Energy card and attach it to Tyranitar.", ability_type=AbilityTypes.POKE_BODY, effect=dp7_tyranitar_30_darkness_drive(), activation=Activations.ONCE_PER_TURN), Attack(title='Grind', game_text='Does 20 damage times the amount of Energy attached to Tyranitar.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=dp7_tyranitar_30_grind()), Attack(title='Spinning Tail', game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.DARKNESS: 5}, effect=damage_all_opponents(30))])
