"""STUB: effect not implemented — do not guess mechanics.
Kabutops (EX12 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import mega_throw
from spirit.game.card_effects.ex import (
    ancient_shell_passive,
    energy_stream,
)

card = PokemonCardDef(guid='e6843db7-c90d-5a2b-af77-7209d7392e99', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name', display_name='Kabutops', searchable_by=['Kabutops', 'Stage 2', 'Kabutops'], subtypes=['Stage 2'], collector_number=7, set_code='EX12', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name', family_id=140, abilities=[Ability(title='Ancient Shell', game_text='As long as you have Omanyte or Omastar in play, damage done to Kabutops by attacks is reduced by 20 (after applying Weakness and Resistance).', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=ancient_shell_passive('Omanyte', 'Omastar', reduce=20)), Attack(title='Energy Stream', game_text='Search your discard pile for a basic Energy card and attach it to Kabutops.', cost={PokemonTypes.FIGHTING: 1}, damage=30, effect=energy_stream()), Attack(title='Extra Claws', game_text='If the Defending Pokémon is Pokémon-ex, this attack does 50 damage plus 30 more damage.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=mega_throw(50, 30))])
