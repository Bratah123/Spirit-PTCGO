from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class OctolockPassive(Passive):
    """Until the carrier (Grapploct) leaves the Active Spot, its locked
    target's attacks cost Colorless Colorless more and it can't retreat."""

    def _locked(self, pokemon, carrier):
        if pokemon.entity_id != getattr(carrier, "_octolock_target_id", None):
            return False
        parent = carrier.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"

    def blocks_retreat(self, pokemon, carrier):
        return self._locked(pokemon, carrier)

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if self._locked(pokemon, carrier):
            cost["Colorless"] = cost.get("Colorless", 0) + 2
        return cost


async def octolock(ctx):
    """Until this Grapploct leaves the Active Spot, the Defending Pokemon's
    attacks cost Colorless Colorless more, and it can't retreat. This effect
    can't be applied more than once."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.attacker._octolock_target_id = defender.entity_id


async def tough_swing(ctx):
    """130. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)

card = PokemonCardDef(
    guid="7ce5897c-5258-5bc4-9bca-0e58f47b223d",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1", "Grapploct"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    passive=OctolockPassive(),
    abilities=[
        Attack(
            title="Octolock",
            game_text="Until this Grapploct leaves the Active Spot, the Defending Pok\u00e9mon's attacks cost ColorlessColorless more, and the Defending Pok\u00e9mon can't retreat. This effect can't be applied more than once.",
            cost={PokemonTypes.FIGHTING: 2},
            effect=octolock,
        ),
        Attack(
            title="Tough Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=tough_swing,
        ),
    ],
)