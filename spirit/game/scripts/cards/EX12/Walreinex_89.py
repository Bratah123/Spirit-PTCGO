"""STUB: effect not implemented — do not guess mechanics.
Walrein ex (EX12 #89): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import (
    ice_throw,
    icy_aura_between_turns,
)

card = PokemonCardDef(guid='4f66d942-9fe0-5aea-9525-24a81b112d73', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Walreinex.Name', display_name='Walrein ex', searchable_by=['Walrein ex', 'Stage 2', 'ex', 'Walreinex'], subtypes=['Stage 2', 'ex'], collector_number=89, set_code='EX12', rarity=Rarities.RareHoloEX, hp=150, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name', family_id=363, abilities=[Ability(title='Icy Aura', game_text="As long as Walrein ex is your Active Pokémon, put 1 damage counter on each Active Pokémon (both yours and your opponent's) between turns, excluding Water Pokémon.", ability_type=AbilityTypes.POKE_BODY, effect=icy_aura_between_turns(), trigger=Triggers.BETWEEN_TURNS), Attack(title='Water Arrow', game_text="Choose 1 of your opponent's Pokémon. This attack does 40 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, effect=snipe_attack(40, pool='any')), Attack(title='Ice Throw', game_text="If the Defending Pokémon is a Fighting Pokémon, this attack's base damage is 120 instead of 80.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2}, damage=80, effect=ice_throw(80, 120))])
