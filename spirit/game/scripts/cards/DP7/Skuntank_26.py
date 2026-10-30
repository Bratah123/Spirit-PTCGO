"""STUB: effect not implemented — do not guess mechanics.
Skuntank (DP7 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp7_skuntank_26_evolutionary_gas,
    dp7_skuntank_26_plunder,
)

card = PokemonCardDef(guid='0c345da7-fe7d-5bda-8d6a-0103f5ca79d9', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Skuntank.Name', display_name='Skuntank', searchable_by=['Skuntank', 'Stage 1', 'Skuntank'], subtypes=['Stage 1'], collector_number=26, set_code='DP7', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name', family_id=434, abilities=[Ability(title='Evolutionary Gas', game_text="Once during your turn (before your attack), when you play Skuntank from your hand to evolve 1 of your Active Pokémon, you may choose 1 of the Defending Pokémon. If that Pokémon tries to attack during your opponent's next turn, that attack does nothing.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_skuntank_26_evolutionary_gas(), activation=Activations.ONCE_PER_TURN), Attack(title='Poison Claws', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=condition_attack(SpecialConditions.POISONED)), Attack(title='Plunder', game_text='Before doing damage, discard all Trainer cards attached to the Defending Pokémon.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp7_skuntank_26_plunder())])
