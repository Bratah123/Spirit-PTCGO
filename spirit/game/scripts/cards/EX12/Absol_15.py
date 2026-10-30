"""STUB: effect not implemented — do not guess mechanics.
Absol (EX12 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import feint_attack
from spirit.game.card_effects.ex import (
    extra_call_ex,
    shining_horn_solo_passive,
)

card = PokemonCardDef(guid='8aa09ee4-ba31-5243-bc59-5a58b9a97829', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name', display_name='Absol', searchable_by=['Absol', 'Basic', 'Absol'], subtypes=['Basic'], collector_number=15, set_code='EX12', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, family_id=359, abilities=[Ability(title='Shining Horn', game_text="As long as Absol is the only Pokémon you have in play, your opponent's Basic Pokémon can't attack.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=shining_horn_solo_passive()), Attack(title='Extra Call', game_text='Search your deck for a Pokémon-ex, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=extra_call_ex()), Attack(title='Feint Attack', game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, effect=feint_attack(20))])
