"""EX12 Legend Maker — Arcanine ex.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import (
    flame_swirl_discard,
    fire_remedy_on_attach,
)

card = PokemonCardDef(guid='d55b2a78-a8ed-597f-aa0a-c57d988370e2', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanineex.Name', display_name='Arcanine ex', searchable_by=['Arcanine ex', 'Stage 1', 'ex', 'Arcanineex'], subtypes=['Stage 1', 'ex'], collector_number=83, set_code='EX12', rarity=Rarities.RareHoloEX, hp=120, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name', family_id=58, abilities=[Ability(title='Fire Remedy', game_text='Whenever you attach a Fire Energy from your hand to Arcanine ex, remove 1 damage counter and all Special Conditions from Arcanine ex.', ability_type=AbilityTypes.POKE_BODY, effect=fire_remedy_on_attach(), trigger=Triggers.ON_ENERGY_ATTACHED), Attack(title='Overrun', game_text="Does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=snipe_attack(20)), Attack(title='Flame Swirl', game_text='Discard 2 Fire Energy or 1 React Energy card attached to Arcanine ex.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=100, effect=flame_swirl_discard())])
