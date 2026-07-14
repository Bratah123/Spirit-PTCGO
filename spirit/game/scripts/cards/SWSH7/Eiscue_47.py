from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive


class BlockfacePassive(Passive):
    """Prevent all damage from attacks by Basic Pokemon."""

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and calc.target is carrier
            and calc.attacker is not None
            and calc.attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        )


async def blockface(ctx):
    """70. During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks from Basic Pokemon."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, BlockfacePassive())


card = PokemonCardDef(
    guid="446961a6-932f-5066-a3a1-bdc019ee4819",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic", "Eiscue"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Blockface",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=blockface,
        ),
    ],
)