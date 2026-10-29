from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import Triggers


from spirit.game.attributes import SpecialConditions


async def hot_poison(ctx):
    """On evolve: you may Burn and Poison the opponent's Active."""
    defender = ctx.opponent_active()
    if defender is None:
        return
    if await ctx.ask_yes_no("Leave the opponent's Active Pokémon Burned and Poisoned?"):
        await ctx.apply_special_condition(defender, SpecialConditions.BURNED)
        await ctx.apply_special_condition(defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="59398bbd-8dd7-5eed-892f-cdb27c1d2c2d",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name",
    display_name="Salazzle",
    searchable_by=["Salazzle", "Stage 1", "Salazzle"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=757,
    abilities=[
        Ability(
            title="Hot Poison",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may leave your opponent's Active Pok\u00e9mon Burned and Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=hot_poison,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)