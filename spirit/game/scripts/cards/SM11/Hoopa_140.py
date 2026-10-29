from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import evil_admonition


async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)
card = PokemonCardDef(guid='2c264a50-44ae-50da-a90b-9f4db2e06a81', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name', display_name='Hoopa', searchable_by=['Hoopa', 'Basic', 'Hoopa'], subtypes=['Basic'], collector_number=140, set_code='SM11', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=720, abilities=[Attack(title='Evil Admonition', game_text="This attack does 20 more damage for each of your opponent's Pokémon that has an Ability.", cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=evil_admonition), Attack(title='Mind Shock', game_text="This attack's damage isn't affected by Weakness or Resistance.", cost={PokemonTypes.COLORLESS: 3}, damage=80, effect=sonic_boom)])
