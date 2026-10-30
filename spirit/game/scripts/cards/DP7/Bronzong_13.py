"""STUB: effect not implemented — do not guess mechanics.
Bronzong (DP7 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_bronzong_13_cycler,
    dp7_bronzong_13_heavy_potential,
    dp7_bronzong_13_strange_spin,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='756069c3-fd06-5541-95b0-17dfca470b5f', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name', display_name='Bronzong', searchable_by=['Bronzong', 'Stage 1', 'Bronzong'], subtypes=['Stage 1'], collector_number=13, set_code='DP7', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.PSYCHIC, resistance_type=PokemonTypes.FIRE, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name', family_id=436, abilities=[Ability(title='Cycler', game_text="Once during your turn (before your attack), you may choose a card from your hand and put it on top of your deck. Then, search your deck for up to 2 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward. This power can't be used if Bronzong is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_bronzong_13_cycler(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Strange Spin', game_text='If you have the same number of cards in your hand as your opponent, this attack does 20 damage plus 40 more damage and the Defending Pokémon is now Confused.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp7_bronzong_13_strange_spin()), Attack(title='Heavy Potential', game_text="Put a number of damage counters on each of your opponent's Pokémon equal to the number of Colorless Energy in that Pokémon's Retreat Cost (after applying effects to the Retreat Cost).", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, effect=dp7_bronzong_13_heavy_potential())])
