from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _Screeched(Passive):
    """Attack damage to this Pokemon is increased by 60 (after W/R)."""
    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.amount > 0 and calc.target is carrier_pokemon(carrier):
            calc.amount += 60


async def _screech(ctx):
    """During your next turn, damage from attacks to the Defending Pokemon is increased by 60."""
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_own_next_turn(d, _Screeched())


card = PokemonCardDef(
    guid="eeb02153-a63e-5e13-925f-00e6ba4b0a6f",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name",
    display_name="Kricketune",
    searchable_by=["Kricketune", "Stage 1", "Kricketune"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    family_id=401,
    abilities=[
        Attack(
            title="Screech",
            game_text="During your next turn, any damage done to the Defending Pok\u00e9mon by attacks is increased by 60 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_screech,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)