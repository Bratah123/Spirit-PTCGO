from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive, effective_max_hp


class DefiantSparkAltCostPassive(Passive):
    """Defiant Spark can be paid with a single [L] once this Pokémon has
    any damage counters on it."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        if cost.get("Lightning") == 2 and cost.get("Colorless") == 1 and len(cost) == 2:
            current = pokemon.get_attribute(AttrID.HP, 0)
            if current < effective_max_hp(board, pokemon):
                return {"Lightning": 1}
        return cost


async def corner(ctx):
    """30 damage. During your opponent's next turn, the Defending Pokémon
    can't retreat."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="519af55e-cc74-52eb-9acc-6ee02ce55067",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boltund.Name",
    display_name="Boltund",
    searchable_by=["Boltund", "Stage 1", "Boltund"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    family_id=835,
    passive=DefiantSparkAltCostPassive(),
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=corner,
        ),
        Attack(
            title="Defiant Spark",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack can be used for Lightning.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)