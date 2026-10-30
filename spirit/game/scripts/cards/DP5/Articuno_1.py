"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp5_articuno_1_blizzard,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='14d9b6be-3576-5b58-9244-d7039be978ec', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name', display_name='Articuno', searchable_by=['Articuno', 'Basic', 'Articuno'], subtypes=['Basic'], collector_number=1, set_code='DP5', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.METAL, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=144, abilities=[Ability(title='Freezing Screech', game_text='Once during your turn, when you put Articuno from your hand onto your Bench, you may flip a coin. If heads, choose 1 of the Defending Pokémon. That Pokémon is now Paralyzed.', ability_type=AbilityTypes.POKE_POWER, effect=condition_attack(SpecialConditions.PARALYZED)), Attack(title='Blizzard', game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Benched Pokémon. If tails, this attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp5_articuno_1_blizzard())])
