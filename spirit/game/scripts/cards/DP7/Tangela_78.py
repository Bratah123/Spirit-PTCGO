"""Tangela (DP7 #78)."""
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import dp7_tangela_78_ingrain

card = PokemonCardDef(
    guid='160c29ae-49a9-5230-a134-ebb978874aba', key='DP7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    display_name='Tangela', searchable_by=['Tangela', 'Basic', 'Tangela'],
    subtypes=['Basic'], collector_number=78, set_code='DP7', rarity=Rarities.Common,
    hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1,
    weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20,
    family_id=114,
    abilities=[
        Attack(title='Ingrain',
               game_text="Flip a coin. If tails, this attack does nothing. If heads, search your deck for a Grass Energy card and attach it to Tangela. Shuffle your deck afterward. If you do, prevent all effects of an attack, including damage, done to Tangela during your opponent's next turn.",
               cost={PokemonTypes.COLORLESS: 1}, effect=dp7_tangela_78_ingrain()),
        Attack(title='Tickle',
               game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.',
               cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20,
               effect=condition_attack(SpecialConditions.PARALYZED, flip=True)),
    ])
