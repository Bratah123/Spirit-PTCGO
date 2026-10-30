"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp5_darkrai_3_dark_resolve,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='d630c6e3-54c5-5942-a9fe-c1391bd1bbe6', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name', display_name='Darkrai', searchable_by=['Darkrai', 'Basic', 'Darkrai'], subtypes=['Basic'], collector_number=3, set_code='DP5', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=491, abilities=[Ability(title='Darkness Shade', game_text='Once during your turn, when you put Darkrai from your hand onto your Bench, you may choose 1 of the Defending Pokémon. That Pokémon is now Asleep.', ability_type=AbilityTypes.POKE_POWER, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Dark Slumber', game_text="At the end of your opponent's next turn, the Defending Pokémon is now Asleep.", cost={PokemonTypes.DARKNESS: 1}, damage=10, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Dark Resolve', game_text='If the Defending Pokémon is Asleep, remove 4 damage counters from Darkrai.', cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp5_darkrai_3_dark_resolve())])
