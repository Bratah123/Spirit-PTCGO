from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.session.passives import Passive


class ScorchingScalesPassive(Passive):
    """Your opponent's Burned Pokémon take 4 damage counters (not 2) between turns."""

    def modify_burn_counters(self, counters, pokemon, carrier):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return counters
        return max(counters, 4)


async def _burning_wind(ctx):
    """Printed damage; you may discard an Energy from this Pokémon to Burn the
    Defending Pokémon."""
    await ctx.deal_damage()
    defender = ctx.defender
    if not ctx.attached_energies(ctx.attacker) or defender is None:
        return
    if not await ctx.ask_yes_no("Discard an Energy from this Pokémon to Burn the Defending Pokémon?"):
        return
    if await ctx.discard_energy_from(ctx.attacker, 1) and not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="aa919215-4e1c-5ec5-92ce-95c21af29a3f",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Ability(
            title="Scorching Scales",
            game_text="Put 4 damage counters instead of 2 on your opponent's Burned Pok\u00e9mon between turns.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=ScorchingScalesPassive(),
        ),
        Attack(
            title="Burning Wind",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_burning_wind,
        ),
    ],
)