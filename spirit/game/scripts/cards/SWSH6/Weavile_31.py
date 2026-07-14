from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.passives import Passive


class TwoHitKOPassive(Passive):
    """During my next turn, a Rapid Strike attack that damages the opponent's
    Active Knocks it Out outright."""

    def __init__(self, owner_player_id):
        self.owner_player_id = owner_player_id

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.amount > 0 and calc.to_active):
            return None
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != self.owner_player_id:
            return None
        if target.owning_player_id == self.owner_player_id:
            return None
        if "Rapid Strike" not in subtypes_for(attacker.archetype_id):
            return None
        current = target.get_attribute(AttrID.HP, 0)
        return max(calc.amount, current)


async def two_hit_ko(ctx):
    """During your next turn, a Rapid Strike attack Knocks Out the Defending Pokemon."""
    ctx.add_passive_through_own_next_turn(
        ctx.attacker, TwoHitKOPassive(ctx.player_id)
    )


card = PokemonCardDef(
    guid="a1e1f2b0-360d-5b4a-a94a-ded80627c938",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Rapid Strike", "Weavile"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=31,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Two-Hit KO",
            game_text="During your next turn, if the Defending Pok\u00e9mon is damaged by an attack from a Rapid Strike Pok\u00e9mon, it will be Knocked Out.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=two_hit_ko,
        ),
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(count=2, minimum=0, reveal=False),
        ),
    ],
)