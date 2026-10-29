from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import effective_retreat_cost
from spirit.game.card_effects.sm11 import ancient_custom_passive


async def _iron_crash(ctx):
    """20 more damage for each Colorless in the opponent's Active's Retreat Cost."""
    target = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, target) if target is not None else 0
    await ctx.deal_damage(ctx.ability.damage + 20 * cost)
card = PokemonCardDef(guid='b994cbad-1c05-5935-ac55-02130746ffee', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name', display_name='Carracosta', searchable_by=['Carracosta', 'Stage 2', 'Carracosta'], subtypes=['Stage 2'], collector_number=45, set_code='SM11', rarity=Rarities.Uncommon, hp=160, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name', family_id=564, abilities=[Ability(title='Ancient Custom', game_text="Pokémon Tool cards attached to your opponent's Pokémon have no effect.", ability_type=AbilityTypes.POKE_ABILITY, passive=ancient_custom_passive), Attack(title='Aqua Impact', game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=80, damage_operator='+', effect=_iron_crash)])
