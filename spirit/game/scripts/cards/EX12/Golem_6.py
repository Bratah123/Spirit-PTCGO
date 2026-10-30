"""STUB: effect not implemented — do not guess mechanics.
Golem (EX12 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    enraged_linear_attack,
    mend_fighting,
)


async def puncture(ctx):
    """This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)
card = PokemonCardDef(guid='a94eeb92-a4e3-5e36-9b4d-d23a480ed15d', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name', display_name='Golem', searchable_by=['Golem', 'Stage 2', 'Golem'], subtypes=['Stage 2'], collector_number=6, set_code='EX12', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name', family_id=74, abilities=[Attack(title='Mend', game_text='Search your discard pile for a Fighting Energy card and attach it to Golem. If you do, remove 2 damage counters from Golem.', cost={PokemonTypes.COLORLESS: 1}, effect=mend_fighting(2)), Attack(title='Enraged Linear Attack', game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage for each damage counter on Golem to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, effect=enraged_linear_attack(10)), Attack(title='Rock Tumble', game_text="This attack's damage isn't affected by Resistance.", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2}, damage=70, effect=puncture)])
