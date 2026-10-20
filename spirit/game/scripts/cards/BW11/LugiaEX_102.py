from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_plasma_energy, plasma_energy_attached


class _OverflowPassive(Passive):
    """If your opponent's Pokemon is Knocked Out by damage from an attack of
    this Pokemon, take 1 more Prize card."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        me = carrier_pokemon(carrier)
        if (me is None or ctx is None or getattr(ctx, "attacker", None) is not me
                or not ctx.is_attack_effect()
                or pokemon.owning_player_id == me.owning_player_id
                or pokemon.entity_id not in getattr(ctx, "attack_damage", {})):
            return count
        return count + 1


async def _plasma_gale(ctx):
    """Discard a Plasma Energy attached to this Pokemon. If you can't, this
    attack does nothing."""
    if not plasma_energy_attached(ctx.attacker):
        return
    gone = await ctx.discard_energy_from(ctx.attacker, 1, predicate=is_plasma_energy, minimum=1,
                                         prompt="Choose a Plasma Energy to discard")
    if gone:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="971a7254-fbb8-5317-a3c7-0ba24364fe45",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name",
    display_name="Lugia-EX",
    searchable_by=["Lugia-EX", "Basic", "EX", "Team Plasma", "LugiaEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=102,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Ability(
            title="Overflow",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from an attack of this Pok\u00e9mon, take 1 more Prize card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_OverflowPassive(),
        ),
        Attack(
            title="Plasma Gale",
            game_text="Discard a Plasma Energy attached to this Pok\u00e9mon. If you can't discard a Plasma Energy, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=_plasma_gale,
        ),
    ],
)